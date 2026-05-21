from django import forms

from .models import User


class UniqueEmailMixin:
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            return email

        queryset = User.objects.filter(email=email)
        if self.instance and self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError("Пользователь с таким email уже зарегистрирован.")
        return email
