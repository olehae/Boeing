from django.shortcuts import render
import sqlite3
from boeing.settings import DATABASES
from email.message import EmailMessage
import ssl
import smtplib
import random
from django.urls import reverse
from django.http import HttpResponseRedirect

def setupemailconnection():
    email_sender = 'boeingproject2023@gmail.com'
    email_authcode = 'rzcvcfvbcrhmennl'

    return email_sender, email_authcode


#setting up the curosor as global variable
def setupdbconnection():
    global connection
    global cursor
    connection = sqlite3.connect(DATABASES['default']['NAME'])
    cursor = connection.cursor()


#creating the table user if it does not exist yet
def create_user_database():
    sql = "CREATE TABLE IF NOT EXISTS user(" \
          "userid INTEGER PRIMARY KEY, " \
          "name TEXT, " \
          "username TEXT, " \
          "email TEXT, " \
          "superuser INTEGER, " \
          "isloggedin INTEGER, " \
          "password TEXT)"
    cursor.execute(sql)
    connection.commit()


 # this function is just for the developement and testing process, doesn't have any real use we need
def delete_table():
    sql = "DROP table user"
    cursor.execute(sql)
    connection.commit()


def create_superuser():
    setupdbconnection()

    name = input('enter name of superuser : ')
    username = input('enter username of superuser : ')
    email = input('enter email of superuser : ')
    password = input('enter password of superuser : ')

    sql = "INSERT INTO user (name, username, email, password, superuser, isloggedin) VALUES (?, ?, ?, ? , 1, 0)"
    cursor.execute(sql, (name, username, email, password))
    connection.commit()


# write the data given by the user into the database and create a new user with that
def write_into_db(signupdata):
    sql = "INSERT INTO user (name, username, email, password, superuser, isloggedin) VALUES (?, ?, ?, ? , 0, 1)"

    try:
        print(signupdata["name"], signupdata['username'], signupdata['email'], signupdata['password'])
        cursor.execute(sql, (signupdata["name"], signupdata['username'], signupdata['email'], signupdata['password']))
        connection.commit()
        print("Succesfully created user!")
        

    except:
        print("Creation of user profile failed!")


def check_user_login(user_login_data):
        print(user_login_data)
        sql = "SELECT * FROM user where username = ? AND password = ?;" # have to swap primary key to username I guess
        cursor.execute(sql, (user_login_data['username'], user_login_data['password']))

        current_user = cursor.fetchall()

        if current_user:
            sql = "UPDATE user SET isloggedin = 1 WHERE username = ?;"
            cursor.execute(sql, (user_login_data['username'],))
            print("login succesful")
            connection.commit()

            return True

        else:
            print("login failed") # leads back to login page
            return False


def send_confirmation_mail(reveiver_address):

    email_sender, email_authcode = setupemailconnection()
    code = random.randint(10000000, 99999999)

    #define subject and mail body
    subject = 'Confirmation Email'
    body = f"""This is your confirmation email with code {code}"""

    #create emailmessage object from emailmassege class and perpare email
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = reveiver_address
    em['Subject'] = subject
    em.set_content(body)
    
    #formating and sending the email via ssl function
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_authcode)
        smtp.sendmail(email_sender, reveiver_address, em.as_string())

    return code