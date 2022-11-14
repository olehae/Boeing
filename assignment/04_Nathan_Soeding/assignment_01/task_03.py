limit = int(input("Give number: "))

n = 0
m = 1
print(n)
print(m)

while not n + m > limit:
    print(n + m)
    m = n + m
    n = m - n
