from django.urls import path
from GardeningApp import views

urlpatterns = [
    # 1) starting from sign up page
    path("signup/", views.signUp, name="signUpPage"),
    path("home/", views.homePage, name="homePage"),
    path("myaccount/", views.homePage, name="accountPage"),
]
