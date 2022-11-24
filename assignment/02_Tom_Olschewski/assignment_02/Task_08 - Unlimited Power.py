def unlimitedpower(base, power):
    if power == 0:
        return 1
    if power == 1:
        return base
    return base * unlimitedpower(base, power-1)

base = int(input("Please enter the base : "))
power = int(input("Please enter the power : "))

result = unlimitedpower(base,power)
print(result)
