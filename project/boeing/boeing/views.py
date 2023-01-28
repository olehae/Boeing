import sqlite3
from django.shortcuts import render
from boeing.settings import DATABASES
from boeing.helperfunctions import get_seat_data


def home(request):
    try:
        username = request.session["username"]
        flight_names = {"flight01": "Berlin - Palma de Mallorca", "flight02": "Hannover - Ibiza",
                        "flight03": "Frankfurt - Paris", "flight04": "Hammensted - Dubai"}

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
            not_needed, one_row = get_seat_data(name)
            left_aisle_seats = one_row[(len(one_row)//2)-1]
            right_aisle_seats = one_row[len(one_row)//2]
            aisle_seats = left_aisle_seats+right_aisle_seats
            window_seats = [one_row[0], one_row[-1]]
            for i in user_data:
                if i[1] in aisle_seats:
                    seat_type = "aisle seat"
                elif i[1] in window_seats:
                    seat_type = "window seat"
                else:
                    seat_type = "middle seat"
                seat = str(flight_names[name]) + ", Row " + str(i[0]) + ", Seat " + str(i[1] + ", Seat type: " + seat_type)
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


def help(request):
    return render(request, "help.html")


def admin(request):
    return render(request, "admin.html")
