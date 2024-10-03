from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Разрешение, которое позволяет доступ только владельцам объекта.

    Это разрешение проверяет, совпадает ли текущий пользователь с владельцем запрашиваемого объекта,
    предоставляя доступ только ему.

    Атрибуты:
    - message (str): Сообщение об ошибке, которое возвращается, если доступ запрещен.

    Методы:
    - has_object_permission(request, view, obj): Проверяет, является ли текущий пользователь владельцем объекта.
    """
    message = 'Это не ваш профиль!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False
