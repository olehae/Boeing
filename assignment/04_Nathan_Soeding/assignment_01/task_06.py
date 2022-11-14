import math

dec = int(input("Give decimal number: "))

x = dec
result = 0

i = 0
while x != 0:
    result += (x % 8) * math.pow(10, i)
    x -= x % 8
    x = x / 8
    i += 1

print(int(result))
