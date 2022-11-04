n = int(input("Please enter your desired Number : "))
fib0 = 0
fib1 = 1

count = 0

while(n>count):
    print(fib0)
    fib1 = fib1 +fib0
    print(fib1)
    fib0 = fib1 + fib0
    count = count + 1
