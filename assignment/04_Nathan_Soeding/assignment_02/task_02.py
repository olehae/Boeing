from random import randint

l = []

for i in range(10):
    l.append(randint(1, 100))

largest = 0
for e in l:
    if e > largest:
        largest = e

print(l)
print(largest)
