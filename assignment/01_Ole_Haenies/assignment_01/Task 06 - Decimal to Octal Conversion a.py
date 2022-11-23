"""
Write a more general program that reads in a non-negative number (potentially including
decimal places) in the decimal representation provided by the user and prints the octal
representation of the number.
"""

while True:
    dec_num = float(input("Please input a non-negative decimal Number: "))
    if dec_num < 0:
        print("Invalid input: The number is negative")
    else:
        break

# first part of number (before .)
oct_num_first = oct(int(dec_num))[2::]
# last part of number (after .)
dec_num_last = dec_num-int(dec_num)

oct_num_last = "."
# Formula: https://de.wikipedia.org/wiki/Oktalsystem
while dec_num_last != int(dec_num_last):
    # add next digit to string oct_num_last
    oct_num_last = oct_num_last + str(int(8 * dec_num_last))
    # redefine dec_num_last as everything but the num in front of the .
    dec_num_last = (8 * dec_num_last) - int(8 * dec_num_last)

# add both strings together, floats would not be as precise because they only have a limited amount of digits
print(oct_num_first + oct_num_last)
