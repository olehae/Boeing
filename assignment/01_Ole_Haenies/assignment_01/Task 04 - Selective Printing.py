"""
Write a program that reads in an upper bound (number) provided by the user and prints all integer
numbers that are less or equal to the upper bound except the integer numbers that are divisible by 3.
Use the continue statement.
"""

upper_bound = int(input("Please input an upper bound nuber: "))

for number in range(upper_bound+1):
    if number % 3 == 0 and number != 0:
        continue
    print(number)