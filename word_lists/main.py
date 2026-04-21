from code_function import occ_word_file_and_reversable


def main():
    rank = None  # add a value if you want

    counter_occ, is_reversable = occ_word_file_and_reversable(
        "top_freq_5000_hu.txt",
        rank
    )

    print(counter_occ[:10])  # change the value if you want
    print(is_reversable)


if __name__ == "__main__":
    main()
