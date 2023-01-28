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
                  "booked_seats": booked_seats,
                  "is_superuser": request.session["superuser"]}

    # a KeyError occurs when request.session["username"] does not exist -> no user is logged in
    except KeyError:
        # if logged_in is False, the html template will not need the other values
        values = {"logged_in": False}

    return render(request, "home.html", values)


def help(request):
    return render(request, "help.html")


def admin(request):
    connection = sqlite3.connect(DATABASES['default']['NAME'])
    cursor = connection.cursor()

    sum_all = 0
    sum_available = 0
    allFlightTables = ["flight01", "flight02", "flight03", "flight04"]
    # For every flight table
    for table in allFlightTables:
        # Gets flight table
        seat_list = cursor.execute("SELECT Occupied FROM {}".format(table)).fetchall()

        # Cleans up the table
        for i in range(len(seat_list)):
            seat_list[i] = seat_list[i][0]

        # Calculates seats
        sum_all += len(seat_list)
        for seat in seat_list:
            if seat == 0:
                sum_available += 1

    # Get user number
    users = cursor.execute("SELECT userid FROM user").fetchall()
    user_count = len(users)

    values = {
        "available": sum_available,
        "available_perc": str(100*sum_available/sum_all)[:5],
        "occupied": sum_all - sum_available,
        "occupied_perc": str(100*(sum_all - sum_available)/sum_all)[:5],
        "user_count": user_count
    }

    connection.close()
    return render(request, "admin.html", values)


# Is called on button click to print stats to text  file
def print_stats(request):
    # Creates new text file and emties it
    text_file = open("stats.txt", 'w')
    text_file.write("")
    text_file.close()
    # Opens the created file
    text_file = open("stats.txt", 'a')

    # Database connection
    connection = sqlite3.connect(DATABASES['default']['NAME'])
    cursor = connection.cursor()

    # Get user data
    users = cursor.execute("SELECT * FROM user").fetchall()

    # Write user data to text file
    text_file.write("User number: " + str(len(users)) + "\n")
    text_file.write("UserID\tName\t\tUsername\tE-mail\t\t\t\t\tSuperuser\n\n")
    for user in users:
        # Doesn't print the password
        for i in range(len(user) - 1):
            text_file.write(str(user[i]))
            # Indents the lines
            indent = 0
            if i == 0 or i == 4:
                indent = 8
            elif i == 1 or i == 2:
                indent = 16
            else:
                indent = 40
            for i in range(indent - len(str(user[i]))):
                text_file.write(" ")
        text_file.write("\n")
    text_file.write("\n")

    # Get seat data
    all_flight_tables = ["flight01", "flight02", "flight03", "flight04"]
    available_seats = []
    occupied_seats = []

    # For every flight
    for table in all_flight_tables:
        # Print available
        text_file.write(table + " AVAILABLE\n")
        text_file.write("Row\tSeat\n")
        available_seats = cursor.execute("SELECT Row, Seat FROM {} WHERE Occupied is FALSE".format(table)).fetchall()
        for seat in available_seats:
            text_file.write(str(seat[0]) + "\t" + str(seat[1]) + "\n")
        text_file.write("\n")

        # Print occupied
        text_file.write(table + " OCCUPIED\n")
        text_file.write("Row\tSeat\tUserID\n")
        occupied_seats = cursor.execute("SELECT Row, Seat, Userid FROM {} WHERE Occupied is TRUE".format(table)).fetchall()
        for seat in occupied_seats:
            text_file.write(str(seat[0]) + "\t" + str(seat[1]) + "\t" + str(seat[2]) + "\n")
        text_file.write("\n")

    text_file.write("Available seats:\n")

    connection.close()
    # Stays on admin page
    return admin(request)
