word = str(input("Please input a word: "))
rev_word = ""
for i in range(len(word)):
    rev_word += word[len(word)-1-i]
print(rev_word)