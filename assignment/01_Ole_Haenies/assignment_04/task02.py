import sys
std = sys.stdout


def remove_long_words(s, n):
    word_list = s.split()
    filtered_list = []
    for i in word_list:
        if len(i) <= n:
            filtered_list.append(i)
    return filtered_list


sys.stdout.write(str(remove_long_words(str(input("Input a string:")), int(input("Input a max word length:")))))
