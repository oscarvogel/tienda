# Generated by Django 3.0.6 on 2020-05-23 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_auto_20200517_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 18, 35, 48, 964390)),
        ),
    ]
