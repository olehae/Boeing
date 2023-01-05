import sys
std = sys.stdout


def remove_long_words(s, n):
    word_list = s.split()
    filtered_list = [word for word in word_list if len(word) <= n]
    return filtered_list


sys.stdout.write(str(remove_long_words(str(input("Input a string:")), int(input("Input a max word length:")))))
