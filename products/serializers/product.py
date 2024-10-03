from rest_framework import serializers

from products.models import Product
from products.validators import validate_release_date


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.

    Сериализатор отвечает за преобразование объектов Product в формат JSON и обратно, а также валидацию данных, поступающих от клиента.

    Атрибуты:
    - Meta: Вложенный класс, который содержит метаданные для сериализатора.
    - model: Указывает, с какой моделью связан данный сериализатор (Product).
    - fields: Кортеж, определяющий поля модели, которые будут включены в сериализацию и десериализацию.
    """
    date_release = serializers.DateField(validators=[validate_release_date])

    class Meta:
        model = Product
        fields = ('pk', 'product_name', 'product_model', 'date_release',)
