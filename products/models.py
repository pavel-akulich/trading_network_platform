from django.db import models

from users.models import NULLABLE


class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='название продукта')
    product_model = models.CharField(max_length=255, verbose_name='модель продукта')
    date_release = models.DateField(verbose_name='дата выхода на рынок', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
