"""
Write a program that reads in a word provided by the user and prints the word in a reversed order. For
example, if the input is hello, the output should be ‘olleh’.
a. Use a loop structure
"""

word = str(input("Please input a word: "))
rev_word = ""
for i in range(len(word)):
    rev_word += word[len(word)-1-i]
print(rev_word)