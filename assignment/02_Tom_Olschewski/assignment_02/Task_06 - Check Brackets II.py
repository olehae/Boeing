def checkbracket(inp, stack):
    if not inp:
        return(stack)
    if inp[0] == "(" or inp[0]  == "{" or inp[0]  == "[":
        stack.append(inp[0])
        return checkbracket(inp[1:], stack)

    if inp[0] == ")" or inp[0]  == "}" or inp[0]  == "]":
        if inp[0] == ")" and stack[-1] != "(": 
            print("The input is mathematically wrong! The brackets overlap!")
            return 1

        if inp[0] == "}" and stack[-1] != "{":
            print("The input is mathematically wrong! The brackets overlap!")
            return 1

        if inp[0] == "]" and stack[-1] != "[":
            print("The input is mathematically wrong! The brackets overlap!")
            return 1

        else:
            stack.pop()
            return checkbracket(inp[1:], stack)


userinput = input("Please enter the mathematical expression you want to check : ")
stack = [] 
result = checkbracket(userinput,stack)

if result: 
    print("Not all brackets were closed properly!")
if not result:
    print("The Input is mathematically correct!")
