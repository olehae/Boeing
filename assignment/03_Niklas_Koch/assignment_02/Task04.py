import random
import numpy as np
from operator import itemgetter

li = []
ls = []

for i in range(10):
    x = np.random.randint(10, 100, size=3)
    t = tuple(x)
    li.append(t)

print(li)

ls = sorted(li, key=itemgetter(2)) 

print(ls)

