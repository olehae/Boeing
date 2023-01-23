from django.shortcuts import render
import sqlite3
from boeing.settings import DATABASES
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from boeing.helperfunctions import send_booking_mail
# Create your views here.


# get data from table
def get_seat_data(table_name):
    # connect to db
    connection = sqlite3.connect(DATABASES['default']['NAME'])
    cursor = connection.cursor()
    seats = cursor.execute("SELECT * FROM {}".format(table_name)).fetchall()
    connection.close()
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

    return output_str


def overview(request):
    flight01 = get_seat_data("flight01")
    flight02 = get_seat_data("flight02")
    flight03 = get_seat_data("flight03")

    return render(request, "overview.html", {"flight01": flight01, "flight02": flight02, "flight03": flight03})


def checkbox(request):
    flight_name = HttpRequest.get_full_path(request).removeprefix("/booking/")
    booked_seats = []

    # connect to db
    connection = sqlite3.connect(DATABASES['default']['NAME'])
    cursor = connection.cursor()

    rows = cursor.execute("SELECT MAX(Row) FROM {} ".format(flight_name)).fetchall()[0][0]
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
                cursor.execute("""UPDATE {} SET Occupied = True, userid = ? WHERE Row = ? AND Seat = ?"""
                               .format(flight_name), (request.session["userid"], booked_row, booked_seat))
                booked_seats.append((booked_row, booked_seat))
                # commit the changes to the database
                connection.commit()

    # get data from chartIn3 table
    data = cursor.execute("SELECT Row, Seat, Occupied FROM {}".format(flight_name)).fetchall()
    connection.close()

    # Get list of Occupied Column
    occupied = [item[2] for item in data]
    # Seat Character and Row Number are added to one string
    seat_char = [str(item[1]) for item in data]
    one_row = list(set(seat_char))
    one_row.sort()
    right_middle_seats = one_row[len(one_row)//2]
    left_middle_seats = one_row[(len(one_row)//2)-1]
    middle_seats = left_middle_seats+right_middle_seats
    window_seats = [one_row[0], one_row[-1]]
    seats = []
    row_counter = 1
    for i, seat in enumerate(seat_char):
        if seat == "A":
            seats.append(int(row_counter))
            row_counter += 1
        if seat == right_middle_seats:
            seats.append("middle")

        if occupied[i]:
            seats.append(str("X"))
        else:
            seats.append(str(seat))

    # the left seats (the numbers) are only needed to format the grid of buttons (<br> before left seat)
    row_number = seats[::int(len(seats) / rows)]

    try:
        if request.session["username"]:
            logged_in = True
        username = request.session["username"]
        # send confirmation email if seats were booked
        if booked_seats:
            send_booking_mail(request.session['email'], flight_name, booked_seats)
            return HttpResponseRedirect(reverse('home'))
    except KeyError:
        logged_in = False
        username = None
    values = {"seats": seats,
              "row_number": row_number,
              "logged_in": logged_in,
              "username": username,
              "middle_seats": middle_seats,
              "window_seats": window_seats}

    # gives values defined above to booking.html file
    return render(request, 'booking.html', values)
