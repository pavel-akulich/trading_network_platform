from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.

    Этот сериализатор управляет преобразованием данных пользователя между форматом JSON и объектом модели User.
    Обрабатывает создание и обновление пользователя, включая безопасное управление паролем.

    Атрибуты:
    - password (CharField): Пароль пользователя. Установлен только для записи и не требуется при создании,
    если пользователь уже существует.

    Методы:
    - create(validated_data): Создает нового пользователя и сохраняет его в базе данных.
    - update(instance, validated_data): Обновляет существующего пользователя. Если передан новый пароль, он устанавливается.
    """
    password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = (
            'pk', 'password', 'email', 'first_name', 'last_name', 'patronymic_name', 'country', 'phone', 'avatar',)
