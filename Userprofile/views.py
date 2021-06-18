from django.shortcuts import render,reverse
# from Userprofile.models import create_user_profile
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User


# Create your views here.
class loginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    authentication_form = AuthenticationForm


    def get_success_url(self):
        return reverse("student:student")


class UserReg(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "signup.html"

    def get_success_url(self):
        return reverse("user:login")




    

