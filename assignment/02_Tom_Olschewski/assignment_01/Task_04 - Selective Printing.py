user_number = int(input("Please enter your desired number : "))

for i in range(user_number+1):
    if i%3 != 0 or i == 0:
        print(i)

    else:
        continue