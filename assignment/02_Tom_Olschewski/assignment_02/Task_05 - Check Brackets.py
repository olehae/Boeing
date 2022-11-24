userinput = input("Please enter the mathematical expression you want to check : ")
stack = [] 

for char in userinput:
    if char == "(":
        stack.append("(")
        #print("Appended (")

    if char == ")":
        if not stack:
            stack.append("false")
            break
        
        else:
            stack.pop()
            #print("Poped )")

if not stack:
    print("The given input is mathematically correct!")

else:
    print("The given input is mathematically incorrect!")
