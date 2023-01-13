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
    global email_sender
    global email_authcode

    email_sender = 'boeingproject2023@gmail.com'
    email_authcode = 'rzcvcfvbcrhmennl'


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
    sql = "INSERT INTO user (name, username, email, password, superuser, isloggedin) VALUES (?, ?, ?, ? , 0, 0)"

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

            return True        # has to link to whatever

        else:
            print("login failed") # leads back to login page
            return False


def send_confirmation_mail(reveiver_address):

    setupemailconnection()
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


def SignUpView(request):

    setupdbconnection()
    create_user_database()
    #delete_table() #just for testing purposes
    #create_superuser() #function to create admin accounts via terminal, rarely used

    rawdata = request.POST
    #print(rawdata)

    try: # this is necessary since the page POST on refresh, and then rawdata is empty and we get an error when trying to define signupdata
        global signupdata
        signupdata = {"name": rawdata['name'],"username": rawdata['username'],"email": rawdata['email'],"password": rawdata['password']}
        #print(signupdata)

        if rawdata['password']  == rawdata['passwordconfirmation']:
            global verification_code
            verification_code = send_confirmation_mail(signupdata['email'])
            return HttpResponseRedirect(reverse('emailconfirmation'))
        
        else:
            return render(request, "registration/signup.html")

    except Exception as e:
        print(e)
        return render(request, "registration/signup.html")


#logs in the user
def LoginView(request):
    setupdbconnection()

    #is_logged_in = {'isloggedin':True}

    #return render(request, "home.html", is_logged_in)
    #return HttpResponseRedirect(reverse('home', kwargs={"isloggedin": is_logged_in}))
    
    try:
        raw_logindata = request.POST
        global user_login_data
        user_login_data = {"username": raw_logindata['username'],"password": raw_logindata['password']}
        is_logged_in = {'isloggedin': check_user_login(user_login_data)}

        if is_logged_in:
            print("hello")
            return render(request, "home.html", is_logged_in)
            #return HttpResponseRedirect(reverse('home'), kwargs=is_logged_in)

    except Exception as e:
        print(e)
        return render(request, "registration/login.html")


    return HttpResponseRedirect(reverse('home'))


#sends confirmation email and confirms it with user
def EmailConfirmationView(request):
    print(verification_code)

    try:
        user_code = request.POST['confirmationcode']
        print(user_code)
        
        if int(user_code) == verification_code:
            print("works fine")
            write_into_db(signupdata)
            return HttpResponseRedirect(reverse('home'))
        else:
            print("Shit failed")
            return HttpResponseRedirect(reverse('signup'))

    except:
        print("no data yet")
        return render(request, "registration/emailconfirmation.html")


def LogoutView(request):
    setupdbconnection()
    try:
        sql = "SELECT username from user where isloggedin = 1;"
        cursor.execute(sql)
        loggedin_user = cursor.fetchall()
    
        connection.commit()
        print(loggedin_user)

        sql = "UPDATE user SET isloggedin = 0 WHERE username = ?;"
        cursor.execute(sql, (loggedin_user[0]))
        connection.commit()

    except:
        print('If nobodys logged in you cant log out')
        return HttpResponseRedirect(reverse('home'))

    return render(request, 'registration/logout.html')