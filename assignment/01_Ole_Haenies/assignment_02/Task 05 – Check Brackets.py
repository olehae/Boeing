"""
Write a program that reads in a string, which is supposed to be a mathematical expression.
Focus on brackets only and check whether left and right brackets are composed correctly.
Ignore all other characters (i.e. you don’t have to check correctness of operators and operands).
"""

while True:
    x = input("Input a mathematical expression:")
    counter = 0
    flag = True
    for i in x:
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1
        if counter<0:
            flag = False
    if counter == 0 and flag:
        print("Correct brackets")
        break
    elif counter == 0 and not flag:
        print("Correct amount of brackets, but some of them are facing the wrong way")
    elif counter != 0:
        print("Incorrect amount of brackets")