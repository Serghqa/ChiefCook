from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
     path("register/", views.RegisterUserView.as_view(), name="register"),
     path("account/", views.AccountView.as_view(), name="account"),
     path("logout/", LogoutView.as_view(), name="logout"),
     path("login/", views.LoginUserView.as_view(), name="login"),
]