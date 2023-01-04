def remove_long_words(test, n):
    word_list = test.split()
    new_list = [word for word in word_list if len(word) <= n]

    return new_list

test = input('Please enter your sentence : ')
n = int(input('Please enter your n : '))

print(remove_long_words(test, n))