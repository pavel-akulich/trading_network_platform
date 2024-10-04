from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    """
    Админ-панель для управления пользователями.

    Этот класс определяет настройки отображения и взаимодействия с
    моделью User в админ-панели Django.

    Атрибуты:
    - list_display (tuple): Поля, которые отображаются в списке пользователей в админ-панели.

    Методы:
    - Использует стандартные методы ModelAdmin для обработки отображения и управления пользователями.
    """
    list_display = ('pk', 'email', 'first_name', 'last_name', 'patronymic_name', 'country', 'phone', 'avatar',)
