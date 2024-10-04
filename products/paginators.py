from rest_framework.pagination import PageNumberPagination


class ProductPaginator(PageNumberPagination):
    """
    Пагинатор для списка продуктов.

    Этот класс управляет пагинацией для API, связанного с продуктами, устанавливая размер страницы и позволяя
    пользователю указывать свой собственный размер страницы через параметр запроса.

    Атрибуты:
    - page_size (int): Количество элементов на странице. По умолчанию 30.
    - page_size_query_param (str): Имя параметра запроса для указания размера страницы. По умолчанию 'page_size'.
    - max_page_size (int): Максимально допустимый размер страницы, который может быть запрошен пользователем.
        """
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 50
