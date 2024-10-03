import qrcode
from io import BytesIO


def generate_qr_code(network):
    """
    Генерирует QR-код с контактными данными сети.

    Функция создает QR-код, содержащий информацию о сети в формате vCard, включая название сети,
    адрес электронной почты и адрес. Сгенерированный QR-код возвращается в виде байтового потока.

    Аргументы:
    - network (Network): Объект сети, содержащий информацию для QR-кода.

    Возвращает:
    - bytes: Изображение QR-кода в формате PNG.
    """

    contact_data = f"""BEGIN:VCARD
VERSION:3.0
FN:{network.network_name}  
EMAIL:{network.email} 
ADR:;;{network.country};{network.city};{network.street};{network.house_number}  
END:VCARD"""

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(contact_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    # Сохраняем изображение в байтовый поток
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return img_io.getvalue()
