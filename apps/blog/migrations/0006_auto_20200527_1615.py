# Generated by Django 3.0.6 on 2020-05-27 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200527_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 27, 16, 15, 29, 573866), verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 27, 16, 15, 29, 573866), verbose_name='Actualizado'),
        ),
    ]