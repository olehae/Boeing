print("Enter as many names as you want, if you want to see who is next in the queue enter 'next'")
names = []
while True:
    name = str(input("Enter a name: ")).lower()
    if name == "next":
        print(names[0])
        names.remove(names[0])
    elif name != "next":
        names.append(name)
    if len(names) == 0:
        break
print("The queue is empty!")
