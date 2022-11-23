userstring = input("Please enter the string you want to analyse : ")
count = {}

userstring = ''.join(userstring.split())

for i in userstring:
    if i not in count:
        count[i] = 0
    count[i] += 1

print("This is how often each character in your string appears : ", count)

