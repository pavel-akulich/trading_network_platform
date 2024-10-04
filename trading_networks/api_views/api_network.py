from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from trading_networks.models import Network
from trading_networks.paginators import NetworkPaginator
from trading_networks.permissions import IsActiveEmployee, IsSuperUser, IsCompanyEmployee
from trading_networks.serializers.network import NetworkSerializer
from trading_networks.tasks import send_qr_code_email
from trading_networks.utils import generate_qr_code


class NetworkCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания новой сети.

    Позволяет аутентифицированным и активным сотрудникам создавать новые объекты сети.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для валидации и сохранения данных сети.
    - permission_classes: Список классов разрешений; доступ разрешен только аутентифицированным и активным сотрудникам.
    """
    serializer_class = NetworkSerializer
    permission_classes = [IsAuthenticated & IsActiveEmployee]


class NetworkListAPIView(generics.ListAPIView):
    """
    Представление для отображения списка всех сетей.

    Позволяет аутентифицированным суперпользователям получать список всех доступных объектов сети,
    с возможностью фильтрации и сортировки.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для представления данных сети.
    - queryset: QuerySet объектов Network, используемых для получения списка.
    - pagination_class: Класс пагинации для управления количеством объектов на странице.
    - permission_classes: Список классов разрешений; доступ разрешен только аутентифицированным суперпользователям.
    - filter_backends: Список бэкендов фильтрации, используемых для обработки фильтрации и сортировки.
    - filterset_fields: Поля, по которым разрешена фильтрация.
    - ordering_fields: Поля, по которым разрешена сортировка.
    """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    pagination_class = NetworkPaginator
    permission_classes = [IsAuthenticated & IsSuperUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('country',)
    ordering_fields = ('network_level',)


class NetworkRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для отображения одной сети по её ID.

    Позволяет аутентифицированным пользователям с активным статусом и сотрудникам компании, а также суперпользователям
    получать детальную информацию о конкретном объекте сети.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для представления данных сети.
    - queryset: QuerySet объектов Network, среди которых производится поиск по ID.
    - permission_classes: Список классов разрешений; доступ разрешен аутентифицированным пользователям с активным статусом,
    сотрудникам компании и суперпользователям.
    """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsAuthenticated & IsActiveEmployee & IsCompanyEmployee | IsSuperUser]


class NetworkUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления существующей сети.

    Позволяет аутентифицированным пользователям с активным статусом и сотрудникам компании, а также суперпользователям
    обновлять информацию о конкретном объекте сети.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для валидации и сохранения обновленных данных сети.
    - queryset: QuerySet объектов Network, среди которых производится поиск по ID.
    - permission_classes: Список классов разрешений; доступ разрешен аутентифицированным пользователям с активным статусом,
    сотрудникам компании и суперпользователям.
    """
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsAuthenticated & IsActiveEmployee & IsCompanyEmployee | IsSuperUser]


class NetworkDestroyAPIView(generics.DestroyAPIView):
    """
    Представление для удаления сети.

    Позволяет аутентифицированным пользователям с активным статусом и сотрудникам компании, а также суперпользователям
    удалять конкретный объект сети.

    Атрибуты:
    - queryset: QuerySet объектов Network, среди которых производится поиск по ID.
    - permission_classes: Список классов разрешений; доступ разрешен аутентифицированным пользователям с активным статусом,
    сотрудникам компании и суперпользователям.
    """
    queryset = Network.objects.all()
    permission_classes = [IsAuthenticated & IsActiveEmployee & IsCompanyEmployee | IsSuperUser]


class NetworkDebtAverageAPIView(generics.ListAPIView):
    """
    Представление для отображения сетей с задолженностью выше средней.

    Позволяет аутентифицированным и активным сотрудникам получать список объектов сети, где задолженность превышает
    среднюю задолженность всех сетей.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для представления данных сети.
    - permission_classes: Список классов разрешений; доступ разрешен только аутентифицированным и активным сотрудникам.
    - pagination_class: Класс пагинации для управления количеством объектов на странице.

    Методы:
    - get_queryset(): Вычисляет среднюю задолженность и фильтрует сети, оставляя те, у которых задолженность больше средней.
    """
    serializer_class = NetworkSerializer
    permission_classes = [IsAuthenticated & IsActiveEmployee]
    pagination_class = NetworkPaginator

    def get_queryset(self):
        # Вычисляем среднюю задолженность
        average_debt = Network.objects.aggregate(Avg('debt'))['debt__avg'] or 0
        # Фильтруем сети с задолженностью выше среднего
        return Network.objects.filter(debt__gt=average_debt)


class NetworkByProductAPIView(generics.ListAPIView):
    """
    Представление для отображения сетей, связанных с определённым продуктом.

    Позволяет аутентифицированным и активным сотрудникам получать список объектов сети, которые связаны
    с указанным продуктом.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для представления данных сети.
    - permission_classes: Список классов разрешений; доступ разрешен только аутентифицированным и активным сотрудникам.
    - pagination_class: Класс пагинации для управления количеством объектов на странице.

    Методы:
    - get_queryset(): Фильтрует сети по ID указанного продукта, возвращая только те, которые связаны с ним.
    """
    serializer_class = NetworkSerializer
    permission_classes = [IsAuthenticated & IsActiveEmployee]
    pagination_class = NetworkPaginator

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        # Фильтруем сети, связанные с указанным продуктом
        return Network.objects.filter(products__id=product_id)


class GenerateQrCodeAPIView(APIView):
    """
    Представление для генерации QR-кода для определённой сети.

    Позволяет аутентифицированным активным сотрудникам компании генерировать QR-код для сети и отправлять его
    на указанный email.

    Атрибуты:
    - permission_classes: Список классов разрешений; доступ разрешен только аутентифицированным, активным сотрудникам компании.

    Методы:
    - get(request, network_id): Генерирует QR-код для указанной сети и отправляет его на email.
    """
    permission_classes = [IsAuthenticated & IsActiveEmployee & IsCompanyEmployee]

    def get(self, request, network_id):
        try:
            network = Network.objects.get(id=network_id)

            if not IsCompanyEmployee().has_object_permission(request, self, network):
                return Response({'error': 'Вы не являетесь сотрудником компании, данные которой хотите получить!'},
                                status=status.HTTP_403_FORBIDDEN)

            qr_code_bytes = generate_qr_code(network)
            send_qr_code_email.delay(request.user.email, qr_code_bytes)

            return Response({'message': 'QR-код успешно сгенерирован и отправлен на ваш email.'},
                            status=status.HTTP_200_OK)
        except Network.DoesNotExist:
            return Response({'error': 'Сеть не найдена.'}, status=status.HTTP_404_NOT_FOUND)
