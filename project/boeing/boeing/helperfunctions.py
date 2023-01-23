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

    email_sender, email_authcode = setupemailconnection()
    code = random.randint(10000000, 99999999)

    # define subject and mail body
    subject = 'Confirmation Email'
    body = f"""This is your confirmation email with code {code}"""

    # create emailmessage object from emailmassege class and perpare email
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


def send_booking_mail(email_address, flight_name, booked_seats):

    email_sender, email_authcode = setupemailconnection()
    seat_list = ""
    for i in booked_seats:
        seat_list += f"- Row: {i[0]}  Seat: {i[1]}\n"

    # define mail body
    body = f"""Thank you for booking the following seats on {flight_name}:\n
{seat_list}\nIf you did not book these seats, you can cancel them by logging into your account."""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_address
    em['Subject'] = f"Booking Confirmation for {flight_name}"
    em.set_content(body)

    # formatting and sending the email via ssl function
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_authcode)
        smtp.sendmail(email_sender, email_address, em.as_string())
