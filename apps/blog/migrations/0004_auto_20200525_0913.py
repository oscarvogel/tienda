# Generated by Django 3.0.6 on 2020-05-25 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200523_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 9, 13, 45, 465622), verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 9, 13, 45, 466625), verbose_name='Actualizado'),
        ),
    ]