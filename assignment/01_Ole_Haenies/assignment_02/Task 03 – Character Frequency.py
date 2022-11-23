"""
Write a program that:
- Reads in a string and removes any spaces from the string
- Counts how often individual characters occur in the string
- Stores the information on character occurrence frequency in a dictionary
- Prints the dictionary.
For example, if the input is “santa claus”, the output should be: {'s': 2, 'a': 3, 'n': 1, 't': 1, 'c': 1, 'l': 1,
'u': 1}.
"""

x = input("Please input a string:").replace(" ", "")
print(x)

def count(x):
    dic = {}
    for i in x:
        if i not in dic:
            dic[i] = 1
        dic[i] += 1
    return dic

def sort(x):
    sorted_dic = {}
    for i in sorted(x.keys()):
        sorted_dic[i] = x[i]
    return sorted_dic

dic = count(x)
dic = sort(dic)

for i in dic:
    print(i, dic[i])