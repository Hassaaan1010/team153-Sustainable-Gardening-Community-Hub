from django.shortcuts import render, redirect
from django.urls import path
from .forms import *
from django.http import HttpResponse

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
            welcomContext = {"new_user_details": request.POST.dict()["userName"]}
            return render(request, "Entry/home.html", welcomContext)

    # if new user has to be registered, blank form will be rendered
    elif request.method == "GET":
        return render(request, "Entry/signUp.html", context)
    return HttpResponse("Invalid Request")


def homePage(request):
    context = {}
    return render(request, "Entry/home.html", context)
