from django.shortcuts import render
import sqlite3
from boeing.settings import DATABASES
# Create your views here.


def overview(request):
    # connect to db
    connection = sqlite3.connect(DATABASES['default']['NAME'])
    cursor = connection.cursor()

    # get data from chartIn3 table
    seats = cursor.execute("SELECT * FROM {}".format("chartIn3")).fetchall()
    seat_set = list(set([i[1] for i in seats]))
    seat_set.sort()
    middle = seat_set[len(seat_set)//2]

    output_str = ""
    for elem in seats:
        if elem[1] == "A":
            output_str += f"\n{elem[0]}\t"
        if elem[1] == middle:
            output_str += " | | "
        if elem[2]:
            output_str += "   "
        else:
            output_str += f" {elem[1]} "

    return render(request, "overview.html", {"flight_name": "chartIn3", "output": output_str})


def checkbox(request):
    # connect to db
    connection = sqlite3.connect(DATABASES['default']['NAME'])
    cursor = connection.cursor()

    # get data from chartIn3 table
    seats = cursor.execute("SELECT Row, Seat, Occupied FROM {}".format("chartIn3")).fetchall()
    rows = 0

    # Get list of Occupied Column
    occupied = [item[2] for item in seats]
    # Seat Character and Row Number are added to one string
    sample_seats = [str(item[1]) for item in seats]
    seats = []
    for i, seat in enumerate(sample_seats):
        if seat == "A":
            seats.append(int(rows+1))
            rows += 1
            if occupied[i]:
                seats.append(str("X"))
            else:
                seats.append(str(seat))
        else:
            if occupied[i]:
                seats.append(str("X"))
            else:
                seats.append(str(seat))
    # this is needed to format the html file if a seat is occupied
    occupied_looking_seats = ["-"+seat+"-" for seat in seats if type(seat) == str]

    # the left seats (Character A) are only needed to format the grid of buttons (<br> before left seat)
    left_seat = seats[::int(len(seats) / rows)]
    middle_seat = seats[int(len(seats)/rows/2)::int(len(seats)/rows)]

    # get a list of all the clicked buttons after the submit button is hit

    for i in range(rows):
        clicked = request.POST.getlist(str(i))
        if clicked:
            for j in clicked:
                # split the strings into row and seat again in order to update their status in the database
                booked_row = int(i)
                booked_seat = str(j)
                print(booked_row)
                print(booked_seat)
                cursor.execute("""UPDATE {} SET Occupied = TRUE WHERE Row = ? AND Seat = ?"""
                            .format("chartIn3"), (booked_row, booked_seat))
                # commit the changes to the database
                connection.commit()

    connection.close()

    values = {"seats": seats, "left_seat": left_seat, "occupied": occupied_looking_seats, "middle_seat": middle_seat}
    # gives values defined above to booking.html file
    return render(request, "booking.html", values)
