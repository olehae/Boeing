userstring = input("Please enter the string you want to know the lenght of : ")

countwithwhitespaces = 0
countwithoutwhitespaces = 0
for char in userstring:
    countwithwhitespaces = countwithwhitespaces + 1
    if char != " ":
        countwithoutwhitespaces = countwithoutwhitespaces + 1

print("This is the lenght of the string you entered with white spaces :", countwithwhitespaces,
      ", and this is it's lenght without whitespaces : ", countwithoutwhitespaces)
