from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда для создания суперпользователя.

    Данная команда создает нового суперпользователя с предопределенными данными.
    Суперпользователь будет иметь полный доступ к административной части приложения.

    Атрибуты:
    - email: Электронная почта пользователя.
    - first_name: Имя пользователя.
    - last_name: Фамилия пользователя.
    - is_staff: Указывает, является ли пользователь сотрудником.
    - is_superuser: Указывает, является ли пользователь суперпользователем.
    - password: Пароль для суперпользователя.
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='example@example.com',
            first_name='first_name',
            last_name='last_name',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('password123')
        user.save()
