import random

nums = []

for i in range(10):
    nums.append(random.randint(1, 100))

print(nums)

def myMax(x):
    m = x[0]
    for i in x:
        if i >= m:
            m = i
    print(m)

myMax(nums)

