import random

from celery import shared_task
from django.core.mail import EmailMessage
from django.db import transaction

from config import settings
from trading_networks.models import Network


@shared_task
def increase_debt():
    """
    Задача увеличивает задолженность перед поставщиком на случайное число от 5 до 500 для всех сетей.

    Эта задача выбирает все существующие сети и увеличивает их задолженность на случайное значение,
    выбираемое в диапазоне от 5 до 500.

    Возвращает строку с информацией о том, на какую сумму увеличена задолженность и для какого количества сетей.
    """
    increase_amount = random.randint(5, 500)
    networks = Network.objects.all()
    updated_count = 0

    for network in networks:
        network.debt += increase_amount
        network.save()
        updated_count += 1

    return f'Увеличено задолженность на {increase_amount} для {updated_count} сетей.'


@shared_task
def decrease_debt():
    """
    Задача уменьшает задолженность перед поставщиком на случайное число от 100 до 10 000 для всех сетей.

    Эта задача выбирает все сети с достаточной задолженностью и уменьшает их задолженность
    на случайное значение, выбираемое в диапазоне от 100 до 10 000.

    Возвращает строку с информацией о том, на какую сумму уменьшена задолженность и для какого количества сетей.
    """
    decrease_amount = random.randint(100, 10000)
    networks = Network.objects.filter(debt__gte=decrease_amount)
    updated_count = 0

    for network in networks:
        network.debt -= decrease_amount
        network.save()
        updated_count += 1

    return f'Уменьшено задолженность на {decrease_amount} для {updated_count} сетей.'


@shared_task
def clear_debt_async(network_ids):
    """
    Асинхронная задача для очистки задолженности перед поставщиком у выбранных сетей.

    Эта задача принимает список идентификаторов сетей и устанавливает задолженность для каждой из них в 0.

    Аргументы:
    - network_ids (list): Список идентификаторов сетей, для которых нужно очистить задолженность.

    Возвращает строку с информацией о том, у скольких сетей была очищена задолженность.
    """
    networks = Network.objects.filter(id__in=network_ids)
    with transaction.atomic():
        updated_count = networks.update(debt=0)
    return f'Задолженность очищена у {updated_count} сетей.'


@shared_task
def send_qr_code_email(email, qr_code_bytes):
    """
    Отправляет QR-код по электронной почте.

    Эта задача создает и отправляет электронное письмо с прикрепленным QR-кодом.
    QR-код содержит контактные данные сети.

    Аргументы:
    - email (str): Электронная почта получателя.
    - qr_code_bytes (bytes): Данные QR-кода, которые будут прикреплены к письму.
    """
    email_subject = 'Ваш QR-код с контактными данными сети'
    email_body = 'Прикрепленный QR-код содержит контактные данные сети.'

    email_message = EmailMessage(subject=email_subject, body=email_body, from_email=settings.EMAIL_HOST_USER,
                                 to=[email])

    email_message.attach('contact.png', qr_code_bytes, 'image/png')

    email_message.send()
