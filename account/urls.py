from django.shortcuts import render
from django.urls import path, include
from . import views

app_name = "account"

urlpatterns = [
    # Registration and verification
    path("register/", views.register_user, name="register"),
    path("email-verification-sent/",
         lambda request: render(request, "account/email/email-verification-sent.html"),  # very easy function
         name="email-verification-sent"),

    # Login and Logout
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    # Dashboard
    path("dashboard/", views.dashboard_user, name="dashboard"),
    path("profile-management/", views.profile_user, name="profile-management"),
    path("delete-user/", views.delete_user, name="delete-user"),
]
