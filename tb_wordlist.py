import urllib.request

#the fllowin function:
    #1. fetches the data (download directly from the GH URL in order to remain flexible
    #2. splits the downloaded text content into a collection of individual words
    #3. excludes all single-letter words
    #4. converts the remaining words to lower case
    #5. stores them in a set object (it will contain unique values only and can run faster as well)
    #6. finds reversible word via looping through each word in the set, reverse the chars, and check if this reversed
        #version of the word also exists in the set
    #7. collects and sorts these words
def get_reversible_words(url):
    #1.
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
    except Exception as e:
        print(f"DOWNLOAD ERROR !: {e}")
        return []

    #2.
    words = content.strip().split()

    #3-4.
    valid_words_set = {word.lower() for word in words if len(word) > 1}

    #5-6.
    result = []
    for word in valid_words_set:
        reversed_word = word[::-1]
        if reversed_word in valid_words_set:
            result.append(word)

    #7
    return sorted(result)


#the raw link to the dataset
raw_url = "https://raw.githubusercontent.com/TaTKcourses/words_practice_2526/main/word_lists/top_freq_5000_hu.txt"

#calling out function
wordslist = get_reversible_words(raw_url)

#lets see them:
print(f"Found {len(wordslist)} words that are the same backwards. These words: \n"
      f"{wordslist}")