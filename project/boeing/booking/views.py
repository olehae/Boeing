from django.shortcuts import render
import sqlite3
from boeing.settings import DATABASES
from boeing.helperfunctions import User
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

    rows = cursor.execute("SELECT MAX(Row) FROM {} ".format("chartIn3")).fetchall()[0][0]
    # get a list of all the clicked buttons after the submit button is hit
    for i in range(1, rows+1):
        # get a list of all the clicked buttons after the submit button is hit
        if str(i) in request.POST.keys():
            clicked = request.POST.getlist(str(i))
        # print(clicked)
        # if clicked:
            for j in clicked:
                # split the strings into row and seat again in order to update their status in the database
                booked_row = int(i)
                booked_seat = str(j)
                # print(booked_row)
                # print(booked_seat)
                cursor.execute("""UPDATE {} SET Occupied = TRUE WHERE Row = ? AND Seat = ?"""
                               .format("chartIn3"), (booked_row, booked_seat))
                # commit the changes to the database
                connection.commit()

    # get data from chartIn3 table
    data = cursor.execute("SELECT Row, Seat, Occupied FROM {}".format("chartIn3")).fetchall()

    # Get list of Occupied Column
    occupied = [item[2] for item in data]
    # Seat Character and Row Number are added to one string
    seat_char = [str(item[1]) for item in data]
    one_row = list(set(seat_char))
    one_row.sort()
    middle = one_row[len(one_row)//2]
    seats = []
    row_counter = 1
    for i, seat in enumerate(seat_char):
        if seat == "A":
            seats.append(int(row_counter))
            row_counter += 1
        if seat == middle:
            seats.append("middle")

        if occupied[i]:
            seats.append(str("X"))
        else:
            seats.append(str(seat))

    # the left seats (the numbers) are only needed to format the grid of buttons (<br> before left seat)
    row_number = seats[::int(len(seats) / rows)]

    connection.close()

    values = {"seats": seats,
              "row_number": row_number,
              "user": User()}
    # gives values defined above to booking.html file
    return render(request, 'booking.html', values)

