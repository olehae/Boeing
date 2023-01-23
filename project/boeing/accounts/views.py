from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import boeing.helperfunctions as hf
from hashlib import sha512


def sign_up_view(request):
    try:
        # set up db connection
        connection = hf.dbconnection()
        cursor = connection.cursor()
        # get all usernames from user table to check if the new one is unique
        all_usernames = [i[0] for i in cursor.execute("SELECT username FROM user").fetchall()]
        if request.POST["username"] in all_usernames:
            return render(request, "registration/signup.html",
                          {"error": "This username already exists, please try a different username"})
        # get all email addresses from user table to check if email is unique
        all_emails = [i[0] for i in cursor.execute("SELECT email FROM user").fetchall()]
        if request.POST["email"] in all_emails:
            return render(request, "registration/signup.html",
                      {"error": "This email already exists, please try to log in to your existing account or create a \
                      new account with a different email"})

        elif str(request.POST['password']) == str(request.POST['passwordconfirmation']):
            # send email with confirmation code
            confirmation_code = hf.send_confirmation_mail(request.POST["email"])
            if not confirmation_code:
                return render(request, "registration/signup.html",
                              {"error": "Invalid Email address, please try again with correct address"})
            print(confirmation_code)
            # encode password with sha512 before writing to signup table
            data = (request.POST["name"], request.POST["username"],
                    request.POST["email"], sha512(str(request.POST["password"]).encode('utf-8')).hexdigest(),
                    str(confirmation_code))
            cursor.execute("INSERT INTO signup (name, username, email, password, authcode) VALUES (?, ?, ?, ?, ?)",
                           data)
            connection.commit()
            connection.close()
            return HttpResponseRedirect(reverse('emailconfirmation'))
        # This else only triggers when the passowrds
        else:
            return render(request, "registration/signup.html",
                          {"error": "Your passwords did not match, please try again"})

    except Exception as e:
        print(e)
        return render(request, "registration/signup.html")


# logs in the user
def login_view(request):
    cursor = hf.dbconnection().cursor()

    if "username" in request.POST.keys() and "password" in request.POST.keys():
        try:
            print(sha512(str(request.POST["password"]).encode('utf-8')).hexdigest())
            user = cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?",
                                  (request.POST['username'],
                                   sha512(str(request.POST["password"]).encode('utf-8')).hexdigest())).fetchall()
            request.session["userid"] = user[0][0]
            request.session["name"] = user[0][1]
            request.session["username"] = user[0][2]
            request.session["email"] = user[0][3]
            request.session["superuser"] = user[0][4]
            request.session.set_expiry(0)  # Session expires when the browser is closed
            return HttpResponseRedirect(reverse('home'))
        except IndexError:
            return render(request, "registration/login.html", {"error": "Incorrect login data"})
    else:
        return render(request, "registration/login.html")


# sends confirmation email and confirms it with user
def email_confirmation_view(request):
    connection = hf.dbconnection()
    cursor = connection.cursor()
    codes = [i[0] for i in cursor.execute("SELECT authcode FROM signup").fetchall()]
    # print(codes)

    # Check if SignUp Button has been clicked
    if "confirmationcode" in request.POST.keys():
        user_code = request.POST['confirmationcode']
        # Check if given code exists in signup table
        if user_code in codes:
            # Get user with given code from signup table
            user = cursor.execute("SELECT * FROM signup WHERE authcode = ?", (str(user_code),)).fetchall()[0]
            # insert user into user table
            cursor.execute("INSERT INTO user (name, username, email, password, superuser) VALUES (?, ?, ?, ? , 0)",
                           (user[0], user[1], user[2], user[3]))
            # delete user from signup table
            cursor.execute("DELETE FROM signup WHERE authcode = ?", (str(user_code),))
            connection.commit()
            missing_values = cursor.execute("SELECT userid, superuser FROM user WHERE username = ? AND password = ?",
                                            (user[1], user[3])).fetchall()[0]
            connection.close()
            request.session["userid"] = missing_values[0]
            request.session["name"] = user[0]
            request.session["username"] = user[1]
            request.session["email"] = user[2]
            request.session["superuser"] = missing_values[1]
            return HttpResponseRedirect(reverse('home'))
        else:
            connection.close()
            print("Incorrect code")
            return render(request, "registration/emailconfirmation.html", {"error": "Incorrect Confirmation Code"})
    else:
        connection.close()
        return render(request, "registration/emailconfirmation.html")


def logout_view(request):
    try:
        del request.session["userid"]
        del request.session["name"]
        del request.session["username"]
        del request.session["email"]
        del request.session["superuser"]

    except Exception as e:
        print(e)
        print('If nobodys logged in you cant log out')
        return HttpResponseRedirect(reverse('home'))

    return HttpResponseRedirect(reverse('home'))
