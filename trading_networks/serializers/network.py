from rest_framework import serializers

from trading_networks.models import Network
from trading_networks.validators import validate_network_supplier, validate_supplier_for_factory


class NetworkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Network.

    Обеспечивает преобразование объектов Network в формат JSON и обратно, а также валидацию данных при создании
    и обновлении сетей.

    Атрибуты:
    - serializer_class: Указывает, что этот сериализатор используется для модели Network.

    Методы:
    - __init__(self, *args, **kwargs): Инициализирует сериализатор, делая поле 'debt' только для чтения,
    если экземпляр уже существует.
    - update(self, instance, validated_data): Обновляет существующий объект Network, исключая поле 'debt' из данных для обновления.
    - validate(self, data): Проводит валидацию данных, используя функции validate_supplier_for_factory и validate_network_supplier.
    - create(self, validated_data): Создает новый объект Network, устанавливая уровень сети и задолженность
    в зависимости от типа сети.

    Класс Meta:
    - model: Модель, с которой связан сериализатор.
    - fields: Поля, которые будут сериализованы.
    - read_only_fields: Поля, которые доступны только для чтения.
    """

    def __init__(self, *args, **kwargs):
        super(NetworkSerializer, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['debt'].read_only = True
        else:
            self.fields['debt'].read_only = False

    def update(self, instance, validated_data):
        validated_data.pop('debt', None)
        return super().update(instance, validated_data)

    def validate(self, data):
        data = validate_supplier_for_factory(data)
        data = validate_network_supplier(data)
        return data

    def create(self, validated_data):

        network_type = validated_data['network_type']
        if network_type == 'Factory':
            validated_data['network_level'] = 0
            validated_data['debt'] = 0
        elif network_type in ['RetailNetwork', 'Distributor', 'DealerCenter', 'IndividualBusinessman']:
            supplier = validated_data.get('supplier')
            if supplier:
                validated_data['network_level'] = supplier.network_level + 1
            else:
                validated_data['network_level'] = 1
        return super().create(validated_data)

    class Meta:

        model = Network
        fields = (
            'pk', 'network_type', 'network_level', 'network_name', 'email', 'country', 'city', 'street', 'house_number',
            'products', 'employees', 'supplier', 'debt', 'created_at',)
        read_only_fields = ('network_level', 'created_at',)
