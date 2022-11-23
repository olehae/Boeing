"""
Write a program that:

Generates a list of 10 tuples, each tuple consisting of 3 random integers between 1 and 100
Sorts the list of tuples in increasing order of the third element in each tuple
Prints the sorted list of tuples
"""

from random import randint

randnum = randint(1, 100)
ls = []
for i in range(10):
    ls.append((randint(1, 100),randint(1, 100),randint(1, 100)))
print("Original List: \n"+str(ls)+"\n")

def sort_by_x_element(list, x):
    x_list = []
    for i in range(len(ls)):
        x_list.append(list[i][x])
    x_list.sort()
    print("Element", x, "sorted in increasing order:")
    print(x_list, "\n")
    sortedlist = []
    for i in x_list:
        for j in list:
            if i == j[x]:
                sortedlist.append(j)
    print("Sorted List:\n"+str(sortedlist))

sort_by_x_element(ls, 2)