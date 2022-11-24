q = [input("Fist name: ")]

while len(q) > 0:
    inp = input("Name or next: ")

    if inp == "next":
        print(q.pop(0))
    else:
        q.append(inp)
