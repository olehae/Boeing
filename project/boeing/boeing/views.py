import sqlite3
from django.shortcuts import render
from boeing.settings import DATABASES


def home(request):
    try:
        if request.session["username"]:
            logged_in = True
        username = request.session["username"]
        # connect to db
        connection = sqlite3.connect(DATABASES['default']['NAME'])
        cursor = connection.cursor()
        booked_seats = []
        flight_names = ("flight01", "flight02", "flight03")
        for name in flight_names:
            user_data = cursor.execute("SELECT Row, Seat FROM {} WHERE Userid = ?".format(name),
                                       (request.session["userid"],)).fetchall()

            for i in user_data:
                seat = str(name) + ", Row " + str(i[0]) + ", Seat " + str(i[1])
                booked_seats.append(seat)
        print(booked_seats)
        connection.close()
    except KeyError:
        logged_in = False
        username = None
        booked_seats = None

    values = {"logged_in": logged_in,
              "username": username,
              "booked_seats": booked_seats}
    return render(request, "home.html", values)
