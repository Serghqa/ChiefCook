from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . forms import UserRegisterForm, UserLoginForm
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
