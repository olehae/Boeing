"""
Write a program that simulates a queue. It will read strings from the input. Consider these inputs as names of people coming to the end of a
queue. Whenever “next” is given as input, the program will print out the name on the turn. The program finishes as soon as the queue is empty.
"""

queue = []

while True:
    name = input("\nInput a new Name or \"next\" to show and remove the first person in the queue: \n")
    if name == "next":
        print("First in Line:", queue.pop(0))

    else:
        queue.append(name)

    print("Current queue:")
    for i, item in enumerate(queue, 1):
        print(f"{i}. {item}")
    if not queue:
        print("The queue is empty")
        break
