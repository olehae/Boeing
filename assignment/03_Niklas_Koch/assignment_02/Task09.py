
def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    a = a * power(a,b-1)
    return a

def factorial(f):
    fac = 1
    while(f>0):
        fac = fac * f
        f = f-1
    return fac

def Taylor(x):
    var = 1
    e = 0
    y = 0
    while (var > 0.000001):
        var = power(x, y) / factorial(y)
        e += var
        y += 1
    return e

p = int(input("Enter a power for e: "))
print(f"e^ {p} = {Taylor(p)}")
    
