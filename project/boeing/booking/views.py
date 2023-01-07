from django.shortcuts import render
import sqlite3
from boeing.settings import DATABASES
# Create your views here.


def index(request):
    # connect to db
    connection = sqlite3.connect(DATABASES['default']['NAME'])
    cursor = connection.cursor()

    # get data from chartIn3 table
    seats = cursor.execute("SELECT Row, Seat FROM chartIn3").fetchall()
    rows = seats[len(seats)-1][0]

    # get the names for one row of seats
    seat_set = [item[1] for item in seats[:int(len(seats)/rows)]]
    connection.close()

    # gives values range(rows) and seat_set to booking.html
    return render(request, "booking.html", {"rows": range(rows), "seat_set": seat_set})
