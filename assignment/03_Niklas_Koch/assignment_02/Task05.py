x = str(input("Enter a mathematical expression: "))
c1 = 0
c2 = 0

for i in x:
    if i == "(":
        c1 += 1
    if i == ")":
        c2 += 1
if c1 == c2:
    print("All brackets are composed correctly!")
elif c1 < c2:
    print(f"{c2 - c1} '(' brackets are missing")
elif c2 < c1:
    print(f"{c1 - c2} ')' brackets are missing")
