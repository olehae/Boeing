from django.shortcuts import render
from boeing.helperfunctions import dbconnection, get_seat_data, get_flights, print_stats
from django.http import HttpResponse, HttpResponseNotFound
import plotly


def home(request):
    if "username" in request.session.keys():
        username = request.session["username"]
        flight_names = get_flights()

        # connect to db
        connection = dbconnection()
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

    # when request.session["username"] does not exist -> no user is logged in
    else:
        # if logged_in is False, the html template will not need the other values
        values = {"logged_in": False}

    return render(request, "home.html", values)


def help(request):
    return render(request, "help.html")


def admin(request):
    # only allow admins (superusers) to open this page
    if "superuser" in request.session.keys() and request.session["superuser"]:
        pass
    else:
        return HttpResponseNotFound()
    # check if download button has been clicked
    if "stats" in request.POST.keys():
        print_stats()
        response = HttpResponse(open("stats.txt", 'rb').read())
        response['Content-Type'] = 'text/plain'
        response['Content-Disposition'] = 'attachment; filename=boeing_stats.txt'
        return response
    connection = dbconnection()
    cursor = connection.cursor()

    sum_all = 0
    sum_available = 0
    all_flight_tables = get_flights().keys()
    # For every flight table
    for table in all_flight_tables:
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

    graphs = []
    for flight in get_flights().keys():
        # get data from tables
        data = cursor.execute("SELECT Occupied from {}".format(flight)).fetchall()
        data = [i[0] for i in data]
        print(len([i for i in data if i]), len([i for i in data if not i]))
        values = [len([i for i in data if i]), len([i for i in data if not i])]
        # plotting the pie chart
        fig = plotly.graph_objs.Figure()
        fig.add_trace(plotly.graph_objs.Pie(labels=["Booked", "Available"], values=values, sort=False))
        fig.update_layout(title=str(flight + ": " + get_flights()[flight]))
        # add pie chart object to graphs list
        graphs.append(plotly.offline.plot(fig, auto_open=False, output_type="div"))

    values = {
        "available": sum_available,
        "available_perc": str(100*sum_available/sum_all)[:5],
        "occupied": sum_all - sum_available,
        "occupied_perc": str(100*(sum_all - sum_available)/sum_all)[:5],
        "user_count": user_count,
        "graphs": graphs,
    }

    connection.close()
    return render(request, "admin.html", values)
