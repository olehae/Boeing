import math
import unittest


def decimal2binary(n):
    # function to convert decimal integers to binary
    x = []
    if n > 0:
        # represents pos numbers
        x.append(1)
    else:
        # represents neg numbers
        x.append(0)
    n = abs(n)

    while n > 0:
        x.append(n % 2)
        n = math.floor(n/2)
    return x[::-1]


# last digit represents sign
print(decimal2binary(5))
