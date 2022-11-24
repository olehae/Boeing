x = int(input("x: "))
n = int(input("n: "))


def rec(b, e):
    if e == 0:
        return 1
    if e == 1:
        return b
    else:
        return rec(b * x, e - 1)


print(rec(x, n))
