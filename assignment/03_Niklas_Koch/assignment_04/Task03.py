import math
def unit_test():
    if decimal2binary(-1) == [1,1] and decimal2binary(0) == [0] and decimal2binary(1) == [0,1] and decimal2binary(2) == [0,1,0] and decimal2binary(3) == [0,1,1]:
        return True
    else:
        return False 

def decimal_to_binary_correct(n):
    temp = n
    n = abs(n)
    x = []
    while n > 0:
        x.append(n % 2)
        n = math.floor(n/2)
    if temp >= 0:
        x.append(0)
    if temp < 0:
        x.append(1)
    return x[::-1]

