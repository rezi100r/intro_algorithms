def find_max_substring(word):
    max_sub_word = ''
    count = 0
    start, end = 0, len(word) - 1

    for c in word:
        if c not in max_sub_word:
            max_sub_word += c
        else:
            if count < len(max_sub_word):
                count = len(max_sub_word)
            max_sub_word = max_sub_word[max_sub_word.index(c) + 1:] + c

    return count if count > len(max_sub_word) else len(max_sub_word)


if __name__ == '__main__':
    word = input()
    print(find_max_substring(word))
