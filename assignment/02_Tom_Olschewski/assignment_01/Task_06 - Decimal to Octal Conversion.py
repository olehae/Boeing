while True:
    decimal = float(input("Please enter a positive number : "))
    if decimal < 0:
        continue
    else:
        break

x = int(decimal // 1)
remainder = decimal % 1
octal = ""
fraction = "0."

while(x >= 8):
    rest = x%8
    x = x // 8
    octal = octal + str(rest)

for i in range(17):
    temp = remainder * 8
    remainder = temp % 1
    fraction = fraction + str(int(temp))

octal = octal + str(x)
octal = str(octal)
octal = octal[::-1]
print(float(octal)+ float(fraction))

"""x=decimal * 8**8     This was with the Method from https://www.rapidtables.com/convert/number/decimal-to-octal.html, didnt work.
octal = ""

while(x >= 8):
    remainder = x%8
    x = x // 8
    octal = octal + str(remainder)      

octal = octal + str(x)
octal = str(octal)
octal = octal[::-1]
print(int(octal))
octal = int(octal) / 8**8

print(f"This is : {decimal} converted to octal : {octal}")"""
