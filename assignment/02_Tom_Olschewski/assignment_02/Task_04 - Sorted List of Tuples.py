import random

listoftuples = []
templist = []

for i in range(0,10):
    for i in range(0,3):
         templist.append(random.randint(1,100))
    listoftuples.append(templist)
    templist = []

print(sorted(listoftuples, key=lambda tuples: tuples[2]))
