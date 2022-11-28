"""
Using function for factorial and function  xn  from previous task, write a program that reads value of x and prints
approximate value of  e^x. Use the Taylor series for calculation. To get precise value of  ex , the series would have
to be infinite. Suppose that there is some required accuracy, so the calculation finishes as soon as the value of the
next element is smaller than given threshold (e.g., 0.000001)
"""

x = int(input("Input x (for e^x): "))


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def taylor(x):
    n = 0
    result = 0
    while power(x, n) / factorial(n) > 0.0001:
        result += power(x, n) / factorial(n)
        n += 1
    return result


print(f"e^{x} = {taylor(x)}")