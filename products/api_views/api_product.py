from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.paginators import ProductPaginator
from products.serializers.product import ProductSerializer
from trading_networks.permissions import IsActiveEmployee, IsSuperUser


class ProductCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания нового продукта.

    Позволяет аутентифицированным и активным сотрудникам добавлять новые продукты.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для преобразования данных продукта в формат JSON.
    - permission_classes: Список классов разрешений; в данном случае доступ разрешен только аутентифицированным и активным сотрудникам.
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class ProductListAPIView(generics.ListAPIView):
    """
    Представление для отображения списка всех продуктов.

    Позволяет аутентифицированным и активным сотрудникам получать список всех продуктов с пагинацией.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для преобразования объектов Product в формат JSON.
    - queryset: QuerySet объектов Product, который возвращает все продукты.
    - pagination_class: Класс пагинации, используемый для разбивки списка продуктов на страницы.
    - permission_classes: Список классов разрешений; доступ разрешен только аутентифицированным и активным сотрудникам.
        """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPaginator
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для отображения детальной информации о продукте.

    Позволяет аутентифицированным и активным сотрудникам получать информацию о конкретном продукте по его ID.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для преобразования объекта Product в формат JSON.
    - queryset: QuerySet объектов Product, среди которых производится поиск по ID.
    - permission_classes: Список классов разрешений; доступ разрешен только аутентифицированным и активным сотрудникам.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления существующего продукта.

    Позволяет аутентифицированным и активным сотрудникам обновлять данные продукта по его ID.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для преобразования данных продукта в формат JSON.
    - queryset: QuerySet объектов Product, среди которых производится поиск по ID.
    - permission_classes: Список классов разрешений; доступ разрешен только аутентифицированным и активным сотрудникам.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """
    Представление для удаления продукта.

    Позволяет аутентифицированным суперпользователям удалять продукт по его ID.

    Атрибуты:
    - queryset: QuerySet объектов Product, среди которых производится поиск по ID.
    - permission_classes: Список классов разрешений; доступ разрешен только аутентифицированным и суперпользователям.
    """
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated & IsSuperUser]
