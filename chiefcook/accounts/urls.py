from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views
from .forms import UserLoginForm


app_name = "accounts"

urlpatterns = [
     path("register/", views.RegisterUserView.as_view(), name="register"),
     path("account/", views.AccountView.as_view(), name="account"),
     path("logout/", LogoutView.as_view(), name="logout"),
     path("login/", LoginView.as_view(template_name="accounts/login.html", authentication_form=UserLoginForm), name="login"),
]