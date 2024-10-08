# Generated by Django 5.1.1 on 2024-10-02 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_type', models.CharField(choices=[('Factory', 'Завод'), ('Distributor', 'Дистрибьютор'), ('DealerCenter', 'Дилерский центр'), ('RetailNetwork', 'Розничная сеть'), ('IndividualBusinessman', 'Индивидуальный предприниматель')], max_length=35, verbose_name='тип сети')),
                ('network_level', models.IntegerField(default=0, verbose_name='уровень в иерархии')),
                ('network_name', models.CharField(max_length=150, verbose_name='название сети')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта сети')),
                ('country', models.CharField(max_length=40, verbose_name='страна')),
                ('city', models.CharField(max_length=40, verbose_name='город')),
                ('street', models.CharField(max_length=80, verbose_name='улица')),
                ('house_number', models.CharField(max_length=20, verbose_name='номер дома')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='задолженность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
            ],
            options={
                'verbose_name': 'сеть',
                'verbose_name_plural': 'сети',
            },
        ),
    ]
