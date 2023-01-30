# This file contains all functions that are called from the various views functions
import sqlite3
from boeing.settings import DATABASES
from email.message import EmailMessage
import ssl
import smtplib
import random


def dbconnection():
    return sqlite3.connect(DATABASES['default']['NAME'])


def setupemailconnection():
    email_sender = 'boeingproject2023@gmail.com'
    email_authcode = 'rzcvcfvbcrhmennl'

    return email_sender, email_authcode


# creating the table user if it does not exist yet
def create_user_database():
    connection = dbconnection()
    cursor = connection.cursor()
    sql = "CREATE TABLE IF NOT EXISTS user(" \
          "userid INTEGER PRIMARY KEY, " \
          "name TEXT, " \
          "username TEXT, " \
          "email TEXT, " \
          "superuser INTEGER, " \
          "password TEXT)"
    cursor.execute(sql)
    connection.commit()


def create_superuser():
    connection = dbconnection()
    cursor = connection.cursor()

    name = input('enter name of superuser : ')
    username = input('enter username of superuser : ')
    email = input('enter email of superuser : ')
    password = input('enter password of superuser : ')

    sql = "INSERT INTO user (name, username, email, password, superuser) VALUES (?, ?, ?, ? , 0)"
    cursor.execute(sql, (name, username, email, password))
    connection.commit()


# write the data given by the user into the database and create a new user with that
def write_into_db(signupdata):
    connection = dbconnection()
    cursor = connection.cursor()
    sql = "INSERT INTO user (name, username, email, password, superuser) VALUES (?, ?, ?, ? , 0)"

    try:
        print(signupdata["name"], signupdata['username'], signupdata['email'], signupdata['password'])
        cursor.execute(sql, (signupdata["name"], signupdata['username'], signupdata['email'], signupdata['password']))
        connection.commit()
        print("Successfully created user!")

    except Exception as e:
        print(e)
        print("Creation of user profile failed!")


def send_confirmation_mail(email_address):
    try:
        email_sender, email_authcode = setupemailconnection()
        code = random.randint(10000000, 99999999)

        # define subject and mail body
        subject = 'Confirmation Email'
        body = f"""This is your confirmation email with code {code}"""

        # create em object from emailmessage class and prepare email
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_address
        em['Subject'] = subject
        em.set_content(body)

        # formatting and sending the email via ssl function
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_authcode)
            smtp.sendmail(email_sender, email_address, em.as_string())

        return code
    except Exception as e:
        print(e)
        return False


def send_booking_mail(email_address, flight_name, booked_seats):

    email_sender, email_authcode = setupemailconnection()
    seat_list = ""
    for i in booked_seats:
        seat_list += f"- Row: {i[0]}  Seat: {i[1]}\n"

    # define mail body
    body = f"""Thank you for booking the following seats on {flight_name} {get_flights()[flight_name]}:\n
{seat_list}\nIf you did not book these seats, you can cancel them by logging into your account."""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_address
    em['Subject'] = f"Booking Confirmation for {flight_name} {get_flights()[flight_name]}"
    em.set_content(body)

    # formatting and sending the email via ssl function
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_authcode)
        smtp.sendmail(email_sender, email_address, em.as_string())


# get data from table
def get_seat_data(table_name):
    # connect to db
    connection = dbconnection()
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
            output_str += " X "
        else:
            output_str += f" {elem[1]} "

    return output_str, seat_set


def get_flights():
    connection = dbconnection()
    cursor = connection.cursor()
    flights_data = cursor.execute("SELECT * FROM flights").fetchall()
    connection.close()
    flights = {}
    for i in flights_data:
        flights[i[0]] = i[1]
    return flights


# Is called on button click to print stats to text file
def print_stats(flights):
    # Reset existing txt file
    text_file = open("stats.txt", 'w')
    text_file.write("")
    text_file.close()
    # Opens the created file
    text_file = open("stats.txt", 'a')

    # Database connection
    connection = dbconnection()
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
            for j in range(indent - len(str(user[i]))):
                text_file.write(" ")
        text_file.write("\n")

    text_file.write("\n\n"+"-"*100+"\n\n\n")  # Section break
    for flight in flights:
        text_file.write(f"{flight.name}\n")
        text_file.write(f"Seats available: {flight.available}\t{flight.available_perc}%\n")
        text_file.write(f"Seats reserved:  {flight.occupied}\t{flight.occupied_perc}%\n\n")

    # Get seat data
    all_flight_tables = get_flights().keys()

    # For every flight
    for table in all_flight_tables:
        text_file.write("\n\n" + "-" * 100 + "\n\n\n")  # Section break
        # Print available
        text_file.write(table + " AVAILABLE\n")
        text_file.write("Row\tSeat\n")
        available_seats = cursor.execute("SELECT Row, Seat FROM {} WHERE Occupied is FALSE"
                                         .format(table)).fetchall()
        for seat in available_seats:
            text_file.write(str(seat[0]) + "\t" + str(seat[1]) + "\n")
        text_file.write("\n")

        # Print occupied
        text_file.write(table + " OCCUPIED\n")
        text_file.write("Row\tSeat\tUserID\n")
        occupied_seats = cursor.execute("SELECT Row, Seat, Userid FROM {} WHERE Occupied is TRUE"
                                        .format(table)).fetchall()
        for seat in occupied_seats:
            text_file.write(str(seat[0]) + "\t" + str(seat[1]) + "\t" + str(seat[2]) + "\n")

    connection.close()
    text_file.close()
