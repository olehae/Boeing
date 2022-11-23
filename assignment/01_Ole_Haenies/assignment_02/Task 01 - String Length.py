"""
Write a program that reads in a string and prints the length of the input string. Do not use any
built-in functions of Python, such as len(). For example, if the input is “Computer Science”, the
output should be length: 16
"""

x = input("Input a string:")
count = 0
for i in x:
    count += 1
print(count)