x = float(input("Input a number: "))
oktal = []
z = x-x//1
x = int(x//1)
while x > 0:
    y = x%8
    x = x//8
    oktal.append(str(y))
oktal.reverse()
if z != 0:
    oktal.append(",")
while z != 0:
    z = z*8
    num = int(z//1)
    z = z-z//1
    oktal.append(str(num))
result = "".join(oktal)
print(result)
