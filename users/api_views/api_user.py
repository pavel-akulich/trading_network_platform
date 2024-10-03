from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from trading_networks.permissions import IsSuperUser
from users.models import User
from users.permissions import IsOwner
from users.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с пользователями.

    Данный класс предоставляет CRUD-операции для модели User с различными разрешениями в зависимости
    от выполняемого действия.

    Атрибуты:
    - serializer_class: Класс сериализатора, используемого для преобразования объектов User в формат JSON.
    - queryset: QuerySet объектов User, используемый для выборки данных из базы.

    Методы:
    - get_permissions(): Определяет разрешения для различных действий (create, list, update, retrieve, destroy).

    Разрешения:
    - create: Доступен любому пользователю (AllowAny).
    - list: Доступен только аутентифицированным пользователям, которые являются суперпользователями.
    - update и partial_update: Доступен аутентифицированным пользователям, которые являются владельцами или суперпользователями.
    - destroy: Доступен аутентифицированным пользователям, которые являются владельцами или суперпользователями.
    - retrieve: Доступен аутентифицированным пользователям, которые являются владельцами или суперпользователями.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated & IsSuperUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated & IsOwner | IsSuperUser]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated & IsOwner | IsSuperUser]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated & IsOwner | IsSuperUser]
        else:
            permission_classes = [IsAuthenticated & IsSuperUser]
        return [permission() for permission in permission_classes]
