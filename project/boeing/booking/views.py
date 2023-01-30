from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from boeing.helperfunctions import dbconnection, send_booking_mail, get_seat_data, get_flights
# Create your views here.


class Flight:
    def __init__(self, name, route, data):
        self.name = name
        self.route = route
        self.data = data


def overview(request):
    flights = [Flight(i, get_flights()[i], get_seat_data(i)[0]) for i in get_flights().keys()]

    return render(request, "overview.html", {"flights": flights})


def checkbox(request):
    if "username" in request.session.keys():
        flight_name = HttpRequest.get_full_path(request).removeprefix("/booking/")
        booked_seats = []

        # connect to db
        connection = dbconnection()
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

        seats = []
        row_counter = 1
        for i, seat in enumerate(seat_char):
            if seat == "A":
                seats.append(int(row_counter))
                row_counter += 1
            if seat == right_middle_seats:
                seats.append("middle")
            # append x if seat is occupied, else append seat
            if occupied[i]:
                seats.append(str("X"))
            else:
                seats.append(str(seat))

        # the left seats (the numbers) are only needed to format the grid of buttons (<br> before left seat)
        row_number = seats[::int(len(seats) / rows)]

        # set logged_in = True if a username exists in the current session
        logged_in = True
        username = request.session["username"]
        # send confirmation email if seats were booked
        if booked_seats:
            send_booking_mail(request.session['email'], flight_name, booked_seats)
            return HttpResponseRedirect(reverse('home'))  # redirect to home if seats were booked
    # when username does not exist in current session -> no user is logged in
    else:
        seats = None
        row_number = None
        logged_in = False
        username = None

    values = {"seats": seats,
              "row_number": row_number,
              "logged_in": logged_in,
              "username": username,
              }

    # gives values defined above to booking.html file
    return render(request, 'booking.html', values)
