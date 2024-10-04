from django.db import models

from products.models import Product
from users.models import NULLABLE, User


class Network(models.Model):
    """
    Модель для представления сети.

    Модель описывает различные типы сетей, такие как заводы, дистрибьюторы и розничные сети.
    Хранит информацию о сети, включая название, адрес, сотрудников и задолженность.

    Атрибуты:
    - network_type (CharField): Тип сети. Может быть одним из предопределенных вариантов.
    - network_level (IntegerField): Уровень сети в иерархии. По умолчанию 0.
    - network_name (CharField): Название сети. Максимальная длина 50 символов.
    - email (EmailField): Электронная почта сети.
    - country (CharField): Страна, в которой расположена сеть. Максимальная длина 40 символов.
    - city (CharField): Город, в котором расположена сеть. Максимальная длина 40 символов.
    - street (CharField): Улица, на которой расположена сеть. Максимальная длина 80 символов.
    - house_number (CharField): Номер дома, в котором расположена сеть. Максимальная длина 20 символов.
    - products (ManyToManyField): Продукты, предлагаемые сетью.
    - employees (ManyToManyField): Сотрудники, работающие в сети. Поле может быть пустым.
    - supplier (ForeignKey): Поставщик сети. Может быть NULL.
    - debt (DecimalField): Задолженность сети. Максимальная длина 20 символов с 2 знаками после запятой.
    - created_at (DateTimeField): Время создания записи о сети. Автоматически устанавливается при создании.

    Методы:
    - __str__(): Возвращает строковое представление объекта Network, отображающее тип, название сети и уровень в иерархии.

    Класс Meta:
    - verbose_name: Человеко-читаемое имя для объекта Network в единственном числе.
    - verbose_name_plural: Человеко-читаемое имя для объектов Network во множественном числе.
    """
    NETWORK_CHOICES = (
        ('Factory', 'Завод'),
        ('Distributor', 'Дистрибьютор'),
        ('DealerCenter', 'Дилерский центр'),
        ('RetailNetwork', 'Розничная сеть'),
        ('IndividualBusinessman', 'Индивидуальный предприниматель')
    )

    network_type = models.CharField(max_length=35, choices=NETWORK_CHOICES, verbose_name='тип сети')
    network_level = models.IntegerField(default=0, verbose_name='уровень в иерархии')
    network_name = models.CharField(max_length=50, verbose_name='название сети')
    email = models.EmailField(verbose_name='электронная почта сети')
    country = models.CharField(max_length=40, verbose_name='страна')
    city = models.CharField(max_length=40, verbose_name='город')
    street = models.CharField(max_length=80, verbose_name='улица')
    house_number = models.CharField(max_length=20, verbose_name='номер дома')
    products = models.ManyToManyField(Product, verbose_name='продукт')
    employees = models.ManyToManyField(User, verbose_name='сотрудник', blank=True)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', related_name='supplied_networks', **NULLABLE)
    debt = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f'{self.network_type} - {self.network_name}, уровень в иерархии - {self.network_level}'

    class Meta:
        verbose_name = 'сеть'
        verbose_name_plural = 'сети'
