from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegisterAdminForm
from .models import User


class ModelUser(UserAdmin):
    add_form = UserRegisterAdminForm
    model = User
    # Поля, которые отображаются в списке всех пользователей
    list_display = ("username", "email", "first_name", "is_staff")

    # Настройки для формы СОЗДАНИЯ (add_form)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'password1', 'password2'),
        }),
    )

    # Настройки для формы РЕДАКТИРОВАНИЯ существующего пользователя
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональные данные', {'fields': ('first_name', 'last_name', 'email', 'avatar', 'bio')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, ModelUser)
