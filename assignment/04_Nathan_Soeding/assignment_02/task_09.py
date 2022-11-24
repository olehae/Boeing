x = int(input("x: "))


def power(b, e):
    if e == 0:
        return 1
    if e == 1:
        return b
    else:
        return power(b * x, e - 1)


def factorial(a):
    multi = 1
    for i in range(a):
        multi *= i + 1
    return multi


last_e_x = -10
e_x = 0
i = 0
while abs(last_e_x - e_x) > 0.000001:
    last_e_x = e_x
    e_x += (power(x, i) / factorial(i))
    i += 1

print(e_x)
