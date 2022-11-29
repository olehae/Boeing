x = str(input("Enter a mathematical expression: "))
cr1 = 0
cr2 = 0
cs1 = 0
cs2 = 0
cc1 = 0
cc2 = 0
for j in x:
    if j != "(" and j != ")" and j != "[" and j != "]" and j != "{" and j != "}":
        x = x.replace(j, "")
    if j == "(":
        cr1 += 1
    if j == ")":
        cr2 += 1
    if j == "[":
        cs1 += 1
    if j == "]":
        cs2 += 1
    if j == "{":
        cc1 += 1
    if j == "}":
        cc2 += 1
print(x)
if "(]" in x or "(}" in x or "[)" in x or "[}" in x or "{)" in x or "{]" in x:
    print("Overlapping expressions in brackets!")
elif cr1 == cr2 and cs1 == cs2 and cc1 == cc2:
    print("All brackets are composed correctly!")
else:
    print("Brackets are missing!")
