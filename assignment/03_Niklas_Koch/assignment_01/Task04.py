x = int(input("Write a number: "))
for i in range(0, x+1):
    if i%3 == 0 and i != 0:
        continue
    else:
        print(i)
