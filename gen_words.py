def load_words_len_x(x) -> set:
    with open("words_alpha.txt", "r") as words:
        return list(filter(None, [len(i) == x and i for i in words.read().split()]))


if __name__ == "__main__":
    x = 5
    # print(load_words_len_x(x))
    print(len(load_words_len_x(x)))
    with open("test.txt", "w") as f:
        f.write("".join(str(w) + "\n" for w in load_words_len_x(x)))