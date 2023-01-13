from django.shortcuts import render
import sqlite3
from boeing.settings import DATABASES
from email.message import EmailMessage
import ssl
import smtplib
import random
from django.urls import reverse
from django.http import HttpResponseRedirect
import boeing.helperfunctions as hf


def SignUpView(request):

    hf.setupdbconnection()
    hf.create_user_database()
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
            verification_code = hf.send_confirmation_mail(signupdata['email'])
            return HttpResponseRedirect(reverse('emailconfirmation'))
        
        else:
            return render(request, "registration/signup.html")

    except Exception as e:
        print(e)
        return render(request, "registration/signup.html")


#logs in the user
def LoginView(request):
    hf.setupdbconnection()

    #is_logged_in = {'isloggedin':True}

    #return render(request, "home.html", is_logged_in)
    #return HttpResponseRedirect(reverse('home', kwargs={"isloggedin": is_logged_in}))
    
    try:
        raw_logindata = request.POST
        global user_login_data
        user_login_data = {"username": raw_logindata['username'],"password": raw_logindata['password']}
        is_logged_in = {'isloggedin': hf.check_user_login(user_login_data)}

        if is_logged_in:
            print("hello")
            return render(request, "home.html", is_logged_in)


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
            hf.write_into_db(signupdata)
            return HttpResponseRedirect(reverse('home'))
        else:
            print("Shit failed")
            return HttpResponseRedirect(reverse('signup'))

    except:
        print("no data yet")
        return render(request, "registration/emailconfirmation.html")


def LogoutView(request):
    connection = sqlite3.connect(DATABASES['default']['NAME'])
    cursor = connection.cursor()
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

    return HttpResponseRedirect(reverse('home'))