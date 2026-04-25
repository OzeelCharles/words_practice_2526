from code_function import occ_word_file_and_reversable


def main():
    rank = 10  # add a value if you want be carefull about lenght of each list

    counter_occ, is_reversable = occ_word_file_and_reversable(
        "top_freq_5000_hu.txt",
        rank
    )
    print('-'*len(str(counter_occ[:rank])))
    print(f"Top {rank} most frequent words:")
    print(counter_occ[:rank])
    print('-'*len(str(counter_occ[:rank])))
    print(f"words among the top {rank} of frequence")
    print("whose reverse also exists in the top 5000:")
    print(is_reversable[:rank])
    print('-'*len(str(counter_occ[:rank])))


if __name__ == "__main__":
    main()
