from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """
    Разрешение, позволяющее доступ только суперпользователям.

    Если пользователь является суперпользователем, разрешается доступ к представлению.

    Атрибуты:
    - message (str): Сообщение об ошибке, отображаемое при отказе в доступе.
    """
    message = 'Вы не суперпользователь!'

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class IsActiveEmployee(BasePermission):
    """
    Разрешение, позволяющее доступ только активным сотрудникам.

    Если пользователь активен, разрешается доступ к представлению.

    Атрибуты:
    - message (str): Сообщение об ошибке, отображаемое при отказе в доступе.
    """
    message = 'Вы не активный сотрудник!'

    def has_permission(self, request, view):
        return request.user.is_active


class IsCompanyEmployee(BasePermission):
    """
    Разрешение, позволяющее доступ только сотрудникам компании (Network).

    Доступ разрешен только в том случае, если пользователь является сотрудником объекта сети, к которому обращается.
    """

    def has_object_permission(self, request, view, obj):
        return request.user in obj.employees.all()
