from django.shortcuts import render


def home(request):
    try:
        if request.session["username"]:
            logged_in = True
        username = request.session["username"]
    except KeyError:
        logged_in = False
        username = None

    return render(request, "home.html", {"logged_in": logged_in, "username": username})
