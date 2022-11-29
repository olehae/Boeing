x = str(input("Enter a string: "))
x = x.replace(" ", "")
y = {}
c = 0
for i in x:
    if i in y:
        y[i] = y[i] + 1
    else:
        y[i] = 1
print(y)
