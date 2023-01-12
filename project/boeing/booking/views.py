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
    rows = seats[len(seats)-1][0]

    # Get list of Occupied Column
    occupied = [item[2] for item in seats]
    # Seat Character and Row Number are added to one string
    seats = [str(item[0])+str(item[1]) for item in seats]
    # this is needed to format the html file if a seat is occupied
    occupied_looking_seats = ["-"+seat+"-" for seat in seats]

    # the left seats (Character A) are only needed to format the grid of buttons (<br> before left seat)
    left_seat = seats[::int(len(seats) / rows)]
    left_seat += ["-"+i+"-" for i in left_seat]
    middle_seat = seats[int(len(seats)/rows/2)::int(len(seats)/rows)]
    print(middle_seat)

    # Mark the occupied seats as "-seat-" example: "0A" is not occupied but "-0A-" is
    for i, status in enumerate(occupied):
        if status:
            seats[i] = "-"+seats[i]+"-"

    # get a list of all the clicked buttons after the submit button is hit
    clicked = request.POST.getlist("check")
    for seat in clicked:
        # split the strings into row and seat again in order to update their status in the database
        booked_row = int(''.join(i for i in seat if i.isdigit()))
        booked_seat = ''.join(i for i in seat if not i.isdigit())
        cursor.execute("""UPDATE {} SET Occupied = TRUE WHERE Row = ? AND Seat = ?"""
                       .format("chartIn3"), (booked_row, booked_seat))
        # commit the changes to the database
        connection.commit()
    connection.close()

    values = {"seats": seats, "left_seat": left_seat, "occupied": occupied_looking_seats, "middle_seat": middle_seat}
    # gives values defined above to booking.html file
    return render(request, "booking.html", values)
