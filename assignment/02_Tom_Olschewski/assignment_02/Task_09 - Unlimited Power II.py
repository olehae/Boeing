def unlimitedpower(base, power):
    if power == 0:
        return 1
    if power == 1:
        return base
    return base * unlimitedpower(base, power-1)

def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i 

    return fac

def taylorseries(x):
    result = 0
    i = 0
    val = 1

    while val > 0.000001:
        val = unlimitedpower(x, i)/factorial(i)
        result += val
        i += 1

    return result

userinput = int(input("Please enter your desired power : "))
print("e**n = : ", taylorseries(userinput))
        
