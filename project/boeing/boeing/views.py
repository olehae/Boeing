import sqlite3
from django.shortcuts import render
from boeing.settings import DATABASES


def home(request):
    try:
        username = request.session["username"]
        flight_names = {"flight01": "Flight 01", "flight02": "Flight 02", "flight03": "Flight 03"}
        print(request.POST)

        # connect to db
        connection = sqlite3.connect(DATABASES['default']['NAME'])
        cursor = connection.cursor()

        for key in request.POST.keys():
            if key == "csrfmiddlewaretoken":
                pass
            else:
                # get flight, row and seat from POST String
                key_list = key.split(", ")
                flight_index = list(flight_names.values()).index(key_list[0])
                flight = list(flight_names.keys())[flight_index]
                row = int(key_list[1].split()[1])
                seat = key_list[2].split()[1]

                # Set Occupied = False (0) and userid = null for the given flight, row and seat
                cursor.execute("""UPDATE {} SET Occupied = False, userid = null WHERE Row = ? AND Seat = ?"""
                               .format(flight), (row, seat))
                # commit the changes to the database
                connection.commit()
        booked_seats = []
        # iterate over all flights (each flight is a different table)
        for name in flight_names.keys():
            # get the seats and rows the logged-in user booked
            user_data = cursor.execute("SELECT Row, Seat FROM {} WHERE Userid = ?"
                                       .format(name), (request.session["userid"],)).fetchall()
            # Save flight name, row and seat into one String to make html part easier
            for i in user_data:
                seat = str(flight_names[name]) + ", Row " + str(i[0]) + ", Seat " + str(i[1])
                booked_seats.append(seat)
        # close db connection
        connection.close()

        # define values who will be given to the html template
        values = {"logged_in": True,
                  "username": username,
                  "booked_seats": booked_seats}

    # a KeyError occurs when request.session["username"] does not exist -> no user is logged in
    except KeyError:
        # if logged_in is False, the html template will not need the other values
        values = {"logged_in": False}

    return render(request, "home.html", values)
