s = input("Give String: ")

count = 0
aus = True
for c in s:
    if c == '(':
        count += 1
    elif c == ')':
        count -= 1

    if count < 0:
        aus = False

if count != 0:
    aus = False

if aus:
    print("correct input")
else:
    print("incorrect input")
