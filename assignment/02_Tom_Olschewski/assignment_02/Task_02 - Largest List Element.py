import random

sample = []
for i in range(0,10):
    sample.append(random.randint(1,100))

currentlargest = sample[0]
for i in sample:
    if currentlargest < i:
        currentlargest = i


print("This is the randomly created list :", sample, "and this is the largest Element it contains :", currentlargest)
