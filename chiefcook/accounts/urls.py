from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
     path("register/", views.RegisterUserView.as_view(), name="register"),
     path("account/", views.AccountView.as_view(), name="account"),
     path("logout/", LogoutView.as_view(), name="logout"),
     path("login/", views.LoginUserView.as_view(), name="login"),
     path("edit-profile/", views.EditAccountView.as_view(), name="edit_profile"),
     path("password-change/", views.UserPasswordChangeView.as_view(), name="password_change"),
     path("password-change-done/", PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html") , name="password_change_done"),
]