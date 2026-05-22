from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .forms import (
    UserRegisterForm,
    UserLoginForm,
    UserUpdateForm,
    UserPasswordChangeForm,
    UserPasswordResetForm,
)
from cooking.models import Recipe


class RegisterUserView(CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/user_register.html"
    success_url = reverse_lazy("accounts:login")


class LoginUserView(LoginView):
    authentication_form = UserLoginForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("accounts:account")


class AccountView(LoginRequiredMixin, ListView):
    template_name = "accounts/account.html"
    context_object_name = "recipes"
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user
        return Recipe.objects.filter(author=user)


class EditAccountView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = "accounts/edit_profile.html"
    success_url = reverse_lazy("accounts:account")

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = "accounts/password_change_form.html"
    success_url = reverse_lazy("accounts:password_change_done")


class UserPasswordResetView(SuccessMessageMixin, PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = "accounts/reset_password.html"
    email_template_name = "accounts/reset_content_email.html"
    success_url = reverse_lazy("accounts:password_reset_done")
    success_message = "Инструкции по востановлению пароля отправлены на вашу почту"


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")
    success_message = "Пароль успешно сохранен"


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"
