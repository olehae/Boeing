"""
Write a program that generates a list of 10 random integers between 1 and 100 and then finds
and prints the largest element in the list. Do not use the built-in function max().
For example, if the input is [23,3,42,29,12,15,8,4,37,34], the output should be the largest element: 42.
"""

from random import randint

ls = []
for i in range(10):
    ls.append(randint(1, 100))
print(ls)

maximum = 0
for i in ls:
    if i > maximum:
        maximum = i
print("Largest element:",maximum)