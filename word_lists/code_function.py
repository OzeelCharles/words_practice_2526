def count_txt_file(file):
    """
    Reads a text file and counts occurrences of valid words.

    A word is considered valid if:
    - it has more than 1 character
    - it contains only alphabetic characters

    The file can contain either:
    - one word per line
    - multiple words separated by commas

    Invalid words are counted separately under '#error_count#'.

    Args:
        file (str): Path to the input text file.

    Returns:
        tuple:
            dict: A dictionary with word counts and an error counter.
                  Example: {"word": 3, "#error_count#": 2}
            set: A set of invalid words encountered in the file.
    """
    error = set()
    res = {"#error_count#": 0}

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # case 1: single word line
            if "," not in line:
                words = [line]
            else:
                words = line.split(",")

            for word in words:
                word = word.strip()

                if len(word) <= 1:
                    continue

                if not word.isalpha():
                    res["#error_count#"] += 1
                    error.add(word)
                    print(f"{word} contain invalid characters")
                    continue

                res[word] = res.get(word, 0) + 1

    return res, error


def max_occ(dict_word: dict, rank: int | None = None):
    """
    Returns words sorted by descending occurrence frequency.

    Args:
        dict_word (dict): Dictionary of word counts.
        rank (int | None): Number of top elements to return.
                           If None, returns all sorted items.

    Returns:
        list: List of tuples (word, count) sorted by count descending.

    Raises:
        TypeError: If dict_word is not a dictionary.
        ValueError: If rank is invalid (<= 0 or too large).
    """
    if not isinstance(dict_word, dict):
        raise TypeError("dict_word must be a dict")

    items = [(k, v) for k, v in dict_word.items() if k != "#error_count#"]
    items = sorted(items, key=lambda x: x[1], reverse=True)

    if rank is None:
        return items

    if rank <= 0 or rank >= len(dict_word):
        raise ValueError(f"rank must be > 0 or <= {len(dict)}")

    return items[:rank]


def keep_word_tuple_occ(list_word_occ: list):
    """
    Extracts only words from a list of (word, count) tuples.

    Args:
        list_word_occ (list): List of tuples (word, occurrence).

    Returns:
        list: List of words only.
    """
    return [word[0] for word in list_word_occ]


def list_wordreversable(list_word: list):
    """
    Filters and returns words that are palindromes.

    A palindrome is a word that reads the same forward and backward.

    Args:
        list_word (list): List of words.

    Returns:
        list: List of palindromic words.
    """
    return [word for word in list_word if word == word[::-1]]


def occ_word_file_and_reversable(file, rank=None):
    """
    Combines file word counting, ranking, and palindrome filtering.

    Steps:
    1. Count word occurrences in a file.
    2. Retrieve top-ranked words.
    3. Extract only the words (ignore counts).
    4. Filter palindromic words.

    Args:
        file (str): Path to the input file.
        rank (int | None): Number of top words to consider.

    Returns:
        tuple:
            list: Top words by frequency.
            list: Palindromic words among them.
    """
    counter, error = count_txt_file(file)

    words = keep_word_tuple_occ(max_occ(counter, rank))
    reversables = list_wordreversable(words)

    return words, reversables
