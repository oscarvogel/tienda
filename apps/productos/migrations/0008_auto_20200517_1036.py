# Generated by Django 3.0.6 on 2020-05-17 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20200517_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 10, 35, 59, 984066)),
        ),
    ]
