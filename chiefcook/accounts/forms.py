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
    email = forms.EmailField(
        required=True,
        label="Почта",
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "placeholder": "Введите email...",
            }
        )
    )
    username = forms.CharField(
        required=True,
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "autocomplete": "username",
                "placeholder": "Придумайте логин...",
            }
        )
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "password1", "password2",)


class UserUpdateForm(UniqueEmailMixin, forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label="Почта",
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "placeholder": "Введите email...",
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = ("avatar", "first_name", "last_name", "bio", "email",)
        widgets = {
            "avatar": CustomClearableFileInput(),
            "first_name": forms.TextInput(
                attrs={
                    "autocomplete": "off",
                    "placeholder": "Введите ваше имя...",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "autocomplete": "off",
                    "placeholder": "Введите вашу фамилию...",
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "placeholder": "Напишите о себе...",
                }
            ),
        }
        labels = {
            "avatar": "Фото",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "bio": "О себе",
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
