"""
Write a function with two arguments –  x  and  n . The function returns the value of  x^n . Use recursion.
"""

x = int(input("Input the x: "))
n = int(input("Input the n: "))

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

print(power(x, n))