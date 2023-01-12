sentence = str(input("Enter a scentence: "))
length = int(input("Enter a number: "))
words = sentence.split()
short_words = [word for word in words if len(word) <= length]
print(short_words)
