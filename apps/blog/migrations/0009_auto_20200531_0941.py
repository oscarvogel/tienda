# Generated by Django 3.0.6 on 2020-05-31 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200527_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 9, 41, 27, 876741), verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 9, 41, 27, 876741), verbose_name='Actualizado'),
        ),
    ]