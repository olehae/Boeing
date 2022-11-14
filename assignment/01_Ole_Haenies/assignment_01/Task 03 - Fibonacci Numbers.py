"""
Write a program that reads in an upper bound (number) provided by the user and prints the sequence
of Fibonacci numbers that are less or equal to the number given by the user. Use a while-loop for this
task.
"""

upper_bound = int(input("Please input an upper bound nuber: "))

n0 = 0
n1 = 1
fibonacci = 1
if upper_bound == 0:
    print(0)
else:
    print(0)
    while fibonacci <= upper_bound:
        print(fibonacci)
        fibonacci = n0 + n1
        n0 = n1
        n1 = fibonacci