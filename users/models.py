from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Пользовательская модель, расширяющая стандартную модель пользователя Django.

    Эта модель заменяет поле `username` на `email` и добавляет дополнительные поля для хранения информации
    о пользователе, включая имя, фамилию, отчество, страну, телефон и аватар.

    Атрибуты:
    - email (EmailField): Уникальный адрес электронной почты, используемый как имя пользователя.
    - first_name (CharField): Имя пользователя. Максимальная длина 30 символов.
    - last_name (CharField): Фамилия пользователя. Максимальная длина 30 символов.
    - patronymic_name (CharField): Отчество пользователя. Максимальная длина 30 символов. Может быть пустым или NULL.
    - country (CharField): Страна пользователя. Максимальная длина 40 символов. Может быть пустой или NULL.
    - phone (CharField): Телефонный номер пользователя. Максимальная длина 20 символов. Может быть пустым или NULL.
    - avatar (ImageField): Аватар пользователя. Загружается в директорию `users_avatar/`. Может быть пустым или NULL.

    Методы:
    - __str__(): Возвращает строковое представление объекта User, отображающее адрес электронной почты.

    Класс Meta:
    - verbose_name: Человеко-читаемое имя для объекта User в единственном числе.
    - verbose_name_plural: Человеко-читаемое имя для объектов User во множественном числе.
    - ordering: Определяет порядок сортировки объектов по первичному ключу.
    """
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    first_name = models.CharField(max_length=30, verbose_name='имя')
    last_name = models.CharField(max_length=30, verbose_name='фамилия')
    patronymic_name = models.CharField(max_length=30, verbose_name='отчество', **NULLABLE)

    country = models.CharField(max_length=40, verbose_name='страна', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users_avatar/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('pk',)
