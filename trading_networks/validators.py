from rest_framework import serializers


def validate_supplier_for_factory(data):
    """
    Проверяет, можно ли указать поставщика для сети типа "Завод".

    Функция проверяет, указан ли поставщик для сети типа "Завод". Если да, то генерируется
    ошибка валидации, так как для данного типа сети поставщик не может быть указан.

    Аргументы:
    - data (dict): Словарь с данными сети, содержащий ключи 'network_type' и 'supplier'.

    Возвращает:
    - dict: Неизмененный словарь с данными, если валидация прошла успешно.
    """
    network_type = data.get('network_type')
    supplier = data.get('supplier')

    if network_type == 'Factory' and supplier:
        raise serializers.ValidationError("Вы не можете указать поставщика для сети типа Завод")
    return data


def validate_network_supplier(data):
    """
    Проверяет уровень сети поставщика.

    Функция проверяет, не достиг ли уровень сети поставщика максимального значения.
    Если уровень поставщика равен или превышает 4, генерируется ошибка валидации.

    Аргументы:
    - data (dict): Словарь с данными сети, содержащий ключ 'supplier'.

    Возвращает:
    - dict: Неизмененный словарь с данными, если валидация прошла успешно.
    """
    supplier = data.get('supplier')
    if supplier and supplier.network_level >= 4:
        raise serializers.ValidationError("Уровень звеньев уже достиг максимума - 5")
    return data
