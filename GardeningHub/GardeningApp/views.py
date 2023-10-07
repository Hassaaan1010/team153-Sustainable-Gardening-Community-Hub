from django.shortcuts import render
from django.urls import path
from .forms import *

# Create your views here.


# 2) signUp page -> starts signup form process
def signUp(request):
    # create blank form
    details_of_SignUpForm = SignUpForm()
    context = {"new_user_details": details_of_SignUpForm}

    # if metho is POST and data is valid->
    # then new user is saved and directed to home/
    if request.method == "POST":
        details_of_SignUpForm = SignUpForm(request.POST)
        if details_of_SignUpForm.is_valid():
            details_of_SignUpForm.save()
            context = {"new_user_details": details_of_SignUpForm}
            return render(request, "home/", context)

    # if new user has to be registered, blank form will be rendered
    elif request.method == "GET":
        return render(request, "Entry/signUp.html", context)


def homePage(request):
    return render(request, "Entry/home.html")
