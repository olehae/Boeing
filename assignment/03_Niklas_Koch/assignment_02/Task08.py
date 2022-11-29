x = int(input("Enter a base: "))
n = int(input("Enter the power: "))

def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    a = a * power(a,b-1)
    return a

print(power(x,n))
