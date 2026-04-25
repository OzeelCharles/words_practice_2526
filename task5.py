# words task 5

# import packages
import requests
# url of top 5k words
url = "https://raw.githubusercontent.com/OzeelCharles/words_practice_2526/main/word_lists/top_freq_5000_hu.txt"
response = requests.get(url)
response.raise_for_status()
top5k = response.text
# change to iterable list
top5k_ls = top5k.split("\n")
# split and append occasional nested lists
for i in top5k_ls:
    if "," in i:
        top5k_ls.append(i.split(","))
# filter out single letter words and remaining lists (duplicates)
top5k_ls = [i for i in top5k_ls if not (type(i) is list or len(i) == 1)]
# set to lowercase
top5k_ls = [i.lower() for i in top5k_ls]
# reverse the filtered list
top5k_ls_rev = [i[::-1] for i in top5k_ls]
# create output
output = []
for i, j in zip(top5k_ls, top5k_ls_rev):
    # check each pair if they are the same and not an empty string
    if i == j and i != "":
        output.append(i)
# show output
print(output)
