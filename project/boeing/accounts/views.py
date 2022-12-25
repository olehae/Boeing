from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm  # builtin form for creating new users in django
    success_url = reverse_lazy("login")  # takes the user to the login page after completing SignUp
    template_name = "registration/signup.html"  # use the signup.html file for user creation
