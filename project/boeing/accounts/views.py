from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import boeing.helperfunctions as hf


def sign_up_view(request):
    # hf.create_user_database()
    # delete_table() #just for testing purposes
    # create_superuser() #function to create admin accounts via terminal, rarely used
    rawdata = request.POST

    # this is necessary since the page POST on refresh,
    # and then rawdata is empty and we get an error when trying to define signupdata
    try:
        global signupdata
        signupdata = {"name": rawdata['name'],
                      "username": rawdata['username'],
                      "email": rawdata['email'],
                      "password": rawdata['password']}

        if rawdata['password'] == rawdata['passwordconfirmation']:
            global verification_code
            verification_code = hf.send_confirmation_mail(signupdata['email'])
            return HttpResponseRedirect(reverse('emailconfirmation'))
        
        else:
            return render(request, "registration/signup.html")

    except Exception as e:
        print(e)
        return render(request, "registration/signup.html")


# logs in the user
def login_view(request):
    cursor = hf.dbconnection().cursor()

    try:
        raw_login = request.POST

        user = cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?",
                              (raw_login['username'], raw_login['password'])).fetchall()
        request.session["userid"] = user[0][0]
        request.session["name"] = user[0][1]
        request.session["username"] = user[0][2]
        request.session["email"] = user[0][3]
        request.session["superuser"] = user[0][4]
        request.session["password"] = user[0][5]
        request.session.set_expiry(0)  # Session expires when the browser is closed
        return HttpResponseRedirect(reverse('home'))

    except Exception as e:
        print(e)
        return render(request, "registration/login.html")

    return HttpResponseRedirect(reverse('home'))


# sends confirmation email and confirms it with user
def email_confirmation_view(request):
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

    except Exception as e:
        print(e)
        print("no data yet")
        return render(request, "registration/emailconfirmation.html")


def logout_view(request):
    try:
        del request.session["userid"]
        del request.session["name"]
        del request.session["username"]
        del request.session["email"]
        del request.session["superuser"]
        del request.session["password"]

    except Exception as e:
        print(e)
        print('If nobodys logged in you cant log out')
        return HttpResponseRedirect(reverse('home'))

    return HttpResponseRedirect(reverse('home'))
