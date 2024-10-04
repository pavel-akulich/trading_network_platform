from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html

from trading_networks.models import Network
from trading_networks.tasks import clear_debt_async


class NetworkAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели Network.

    Позволяет администратору управлять сетями, предоставляя интерфейс для отображения, фильтрации и изменения
    информации о сетях.

    Атрибуты:
    - list_display: Список полей, отображаемых в таблице сетей на странице администрирования.
    - list_filter: Поля, по которым можно фильтровать списки сетей.
    - readonly_fields: Поля, которые доступны только для чтения в форме редактирования.
    - search_fields: Поля, по которым можно выполнять поиск сетей.
    - ordering: Порядок сортировки при отображении сетей.
    - actions: Список действий, доступных для выполнения над выделенными объектами.

    Методы:
    - supplier_link(self, obj): Создает ссылку на поставщика, если он существует.
    - clear_debt(self, request, queryset): Очищает задолженность для выбранных сетей. Если выбрано более 20 сетей,
    задолженность очищается асинхронно.
    """
    list_display = ('pk', 'network_type', 'network_name', 'email', 'copy_email', 'city', 'debt', 'created_at', 'supplier_link')
    list_filter = ('city',)
    readonly_fields = ('network_level',)
    search_fields = ('network_name', 'city', 'supplier__network_name')
    ordering = ('pk',)
    actions = ['clear_debt']

    def supplier_link(self, obj):
        """
        Создает ссылку на поставщика.

        Если у сети есть поставщик, возвращает HTML-код для ссылки на
        страницу деталей поставщика. Если поставщика нет, возвращает "-".
        """
        if obj.supplier:
            url = f'/api/networks/detail/{obj.supplier.id}'
            return format_html('<a href="{}">{}</a>', url, obj.supplier.network_name)
        return "-"

    supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        """
        Очищает задолженность для выбранных сетей.

        Если выбрано более 20 сетей, задолженность очищается асинхронно.
        В противном случае задолженность очищается синхронно.
        """
        selected = queryset.count()
        if selected > 20:
            network_ids = list(queryset.values_list('id', flat=True))
            clear_debt_async.delay(network_ids)
            self.message_user(request, f'Очистка задолженности для {selected} сетей запущена асинхронно.',
                              level=messages.INFO)
        else:
            updated_count = queryset.update(debt=0)
            self.message_user(request, f'Задолженность очищена у {updated_count} сетей.', level=messages.SUCCESS)

    clear_debt.short_description = 'Очистить задолженность перед поставщиком'

    def copy_email(self, obj):
        """
        Создает кнопку для копирования электронной почты.
        """
        return format_html(
            '<button class="copy-email-btn" data-email="{}">Копировать</button>',
            obj.email
        )

    copy_email.short_description = 'скопировать почту'
    copy_email.allow_tags = True

    class Media:
        js = ('admin/js/copy_email.js',)
        css = {
            'all': ('admin/css/custom_admin_styles.css',)
        }

admin.site.register(Network, NetworkAdmin)
