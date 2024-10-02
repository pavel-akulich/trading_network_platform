from django.db import models

from products.models import Product
from users.models import NULLABLE, User


class Network(models.Model):
    NETWORK_CHOICES = (
        ('Factory', 'Завод'),
        ('Distributor', 'Дистрибьютор'),
        ('DealerCenter', 'Дилерский центр'),
        ('RetailNetwork', 'Розничная сеть'),
        ('IndividualBusinessman', 'Индивидуальный предприниматель')
    )

    network_type = models.CharField(max_length=35, choices=NETWORK_CHOICES, verbose_name='тип сети')
    network_level = models.IntegerField(default=0, verbose_name='уровень в иерархии')
    network_name = models.CharField(max_length=150, verbose_name='название сети')
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
