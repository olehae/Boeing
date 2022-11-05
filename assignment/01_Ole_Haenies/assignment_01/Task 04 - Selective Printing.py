upper_bound = int(input("Please input an upper bound nuber: "))

for number in range(upper_bound+1):
    if number % 3 == 0 and number != 0:
        continue
    print(number)