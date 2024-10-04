from django.db import models

from users.models import NULLABLE


class Product(models.Model):
    """
    Модель для представления продукта.

    Модель описывает продукт с его названием, моделью и датой выхода на рынок. Используется для хранения информации
    о продуктах в системе.

    Атрибуты:
    - product_name (CharField): Название продукта. Максимальная длина 25 символов.
    - product_model (CharField): Модель продукта. Максимальная длина 25 символов.
    - date_release (DateField): Дата выхода продукта на рынок. Может быть пустым или NULL (определяется в NULLABLE).

    Методы:
    - __str__(): Возвращает строковое представление объекта Product, отображающее название продукта.

    Класс Meta:
    - verbose_name: Человеко-читаемое имя для объекта Product в единственном числе.
    - verbose_name_plural: Человеко-читаемое имя для объектов Product во множественном числе.
    """
    product_name = models.CharField(max_length=25, verbose_name='название продукта')
    product_model = models.CharField(max_length=25, verbose_name='модель продукта')
    date_release = models.DateField(verbose_name='дата выхода на рынок', **NULLABLE)

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
