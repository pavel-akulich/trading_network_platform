from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Административное представление для модели Product.

    Этот класс настраивает интерфейс администратора для управления объектами модели Product. Позволяет администраторам
    просматривать и редактировать данные о продуктах в удобном интерфейсе.

    Атрибуты:
    - list_display: Кортеж, определяющий, какие поля модели будут отображаться в списке объектов на странице администратора.
        """
    list_display = ('pk', 'product_name', 'product_model', 'date_release',)
