# Generated by Django 4.0.5 on 2022-06-29 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folha_pagamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('codigo_cargo', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('cargo', models.CharField(default='', max_length=100)),
                ('salario_base', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(default='', max_length=11, unique=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cargo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='folha_pagamento.Cargos'),
        ),
    ]