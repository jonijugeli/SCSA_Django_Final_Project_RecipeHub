# users/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register_view, login_view, profile_view, CustomLogoutView

app_name = "users"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),


]
