"""
Write a program that reads in a string, which is supposed to be a mathematical expression. Focus on brackets only and check whether left and
right brackets are composed correctly. Ignore all other characters (i.e. you don’t have to check correctness of operators and operands)
"""

while True:
    x = input("Input a mathematical expression (or break to stop): \n")
    if x == "break":
        break

    brackets = ""
    counter = 0
    done = False

    for i in x:
        if i in ["(", ")", "[", "]", "{", "}"]:
            brackets += i
            if i in ["(", "[", "{"]:
                counter += 1
            elif i in [")", "]", "}"]:
                counter -= 1
    print("Brackets only:", brackets)
    if counter != 0:
        print("Incorrect amount of brackets")
    else:
        while brackets != "":
            temp = brackets
            brackets = brackets.replace("()", "")
            brackets = brackets.replace("[]", "")
            brackets = brackets.replace("{}", "")
            if temp == brackets and temp != "":     # If this is the case, no brackets were removed
                print("Incorrect brackets (brackets can not overlap)")
                break
            else:
                print("Correct brackets")
                done = True
                break
    if done:
        break
