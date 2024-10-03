from rest_framework import serializers
from datetime import date

def validate_release_date(value):
    """
    Проверяет, что вводимая дата не новее сегодняшней.

    Аргументы:
    - value: Дата, переданная для проверки.

    Исключение:
    - serializers.ValidationError: Выдается, если дата новее сегодняшней.
    """
    if value > date.today():
        raise serializers.ValidationError("Дата выпуска не может быть новее сегодняшней!")
    return value
