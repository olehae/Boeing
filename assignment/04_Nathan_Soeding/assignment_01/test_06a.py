import math

dec = float(input("Give decimal int or float number: "))

# Calculates the digits before the dot
x = int(dec)
int_result = 0

i = 0
while x != 0:
    int_result += (x % 8) * math.pow(10, i)
    x -= x % 8
    x = x / 8
    i += 1

# Calculates the digits after the dot
y = dec - int(dec)
float_result = 0

j = 0
while y != 0:
    y = y * 8
    float_result += int(y) * (1 / math.pow(10, j + 1))
    y -= int(y)
    j += 1

# Merges the result from both calculations
print(int_result + float_result)
