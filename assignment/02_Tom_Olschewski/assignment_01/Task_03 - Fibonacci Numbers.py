n = int(input("Please enter your desired Number : "))
fib0 = 0
fib1 = 1

while(n>fib1 and n>fib0):
    print(fib0)
    fib1 = fib1 +fib0

    if n>fib1:
        print(fib1)
        fib0 = fib1 + fib0

