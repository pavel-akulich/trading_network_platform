# Generated by Django 5.1.1 on 2024-10-02 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, verbose_name='название продукта')),
                ('product_model', models.CharField(max_length=255, verbose_name='модель продукта')),
                ('date_release', models.DateField(blank=True, null=True, verbose_name='дата выхода на рынок')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
