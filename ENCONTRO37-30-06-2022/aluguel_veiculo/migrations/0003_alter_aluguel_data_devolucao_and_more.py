# Generated by Django 4.0.5 on 2022-06-30 23:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel_veiculo', '0002_rename_cliente_aluguel_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='data_devolucao',
            field=models.DateField(default=datetime.datetime(2022, 6, 30, 23, 28, 24, 374595, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='data_retirada',
            field=models.DateField(default=datetime.datetime(2022, 6, 30, 23, 28, 24, 374595, tzinfo=utc)),
        ),
    ]