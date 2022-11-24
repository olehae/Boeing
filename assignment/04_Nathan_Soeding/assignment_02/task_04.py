from random import randint

l = []

for i in range(10):
    l.append((randint(1, 100), randint(1, 100), randint(1, 100)))
print(l)

thirds = []
for i in range(len(l)):
    thirds.append(l[i][2])
thirds = sorted(thirds)

sorted_list = []
while len(thirds) > 0:
    for e in l:
        if e[2] == thirds[0]:
            sorted_list.append(e)
            l.remove(e)
    thirds.pop(0)

print(sorted_list)
