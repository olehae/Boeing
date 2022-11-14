limit = int(input("Give number: "))

for i in range(limit):
    if i % 3 == 0:
        continue
    print(i)
