num = int(input("Input a number: "))
x = 0
y = 1
z = 1
print(x)
while z < num:
    x = x + y
    print(y)
    z += 1
    if z < num:
        y = x + y
        print(x)        
        z += 1

