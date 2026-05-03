from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import reverse_lazy

from . forms import UserRegisterForm
from cooking.models import Profile


class RegisterUserView(CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/user_register.html"
    success_url = reverse_lazy("accounts:account")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        Profile.objects.create(user=user)
        login(self.request, user)

        return response


class AccountView(LoginRequiredMixin, DetailView):
    template_name = "accounts/account.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        return self.request.user.profile
