s = input("Give String: ")

for c in s:
    if c != '(' and c != ')' and c != '[' and c != ']' and c != '{' and c != '}':
        s = s.replace(c, "")

last_string = ""
# Removes open and closed brackets of the same type that are next to each other
# If the string doesn't change after an iteration, and it isn't empty the input was wrong
while not len(s) == 0 and last_string != s:
    last_string = s

    s = s.replace("()", "")
    s = s.replace("[]", "")
    s = s.replace("{}", "")

if len(s) > 0:
    print("incorrect input")
else:
    print("correct input")
