word = input("Please enter your word : ")
reversed_word = ""

print("This is the loop based approach.")
for i in word:
    reversed_word = i + reversed_word
    print(reversed_word)

reversed_word2 = word[::-1]
print("\nThis is the reverse approach with just the index [::-1] : ", reversed_word2)