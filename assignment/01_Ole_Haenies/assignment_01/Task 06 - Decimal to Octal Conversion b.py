while True:
    dec_num = int(input("Please input a non-negative decimal Number: "))
    if dec_num < 0:
        print("Invalid input: The number is negative")
    else:
        break

# oct(dec_num) is a string, the first two digits are always 0o
oct_num = int(oct(dec_num)[2::])

print(oct_num)