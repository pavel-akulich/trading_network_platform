from rest_framework.pagination import PageNumberPagination


class NetworkPaginator(PageNumberPagination):
    """
    Пагинатор для списка сетей.

    Данный пагинатор управляет пагинацией в API, позволяя разбивать наборы данных на страницы.

    Атрибуты:
    - page_size (int): Количество объектов на странице. По умолчанию 15.
    - page_size_query_param (str): Параметр запроса для указания количества объектов на странице.
    - max_page_size (int): Максимально допустимое количество объектов на странице.
    """
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 30
