from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

from .utils import UniqueEmailMixin
from .widgets import CustomClearableFileInput
from .models import User


class UserRegisterAdminForm(UniqueEmailMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name",)


class UserRegisterForm(UniqueEmailMixin, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True
        self.fields["first_name"].required = True

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "first_name",)
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "autocomplete": "email",
                    "placeholder": "Введите email...",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "autofocus": True,
                    "autocomplete": "username",
                    "placeholder": "Придумайте логин...",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "autocomplete": "given-name",
                    "placeholder": "Ваше имя",
                    "required": True,
                }
            ),
        }


class UserUpdateForm(UniqueEmailMixin, forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("avatar", "first_name", "last_name", "bio", "email",)
        widgets = {
            "avatar": CustomClearableFileInput(),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Введите логин...",
            }
        )
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "placeholder": "Введите пароль...",
            }
        )
    )
