peopleinqueue = input("Please enter the first digit of the names you'd like to enter into the queue : ")

while True:
    if not peopleinqueue:
        print("The queue is now empty, programm will exit.")
        break

    print("This is the current queue :", peopleinqueue)
    iterativeinput = input("Please say next to call the next person in queue or add new names to the queue : ")

    if iterativeinput == "next":
        peopleinqueue = peopleinqueue[1:]
        print(peopleinqueue)
    
    else:
        peopleinqueue += (iterativeinput)
