while True:
    dec_num = float(input("Please input a non-negative decimal Number: "))
    if dec_num < 0:
        print("Invalid input: The number is negative")
    else:
        break

# first part of number (before .)
oct_num_first = int(oct(int(dec_num))[2::])
# last part of number (after .)
dec_num_last = dec_num-int(dec_num)

oct_num_last = "0."
# Formula: https://de.wikipedia.org/wiki/Oktalsystem
while dec_num_last != int(dec_num_last):
    # add next digit to string oct_num_last
    oct_num_last = oct_num_last + str(int(8 * dec_num_last))
    # redefine dec_num_last as everything but the num in front of the .
    dec_num_last = (8 * dec_num_last) - int(8 * dec_num_last)

# oct_num_last was a string in the while loop
print(oct_num_first + float(oct_num_last))
