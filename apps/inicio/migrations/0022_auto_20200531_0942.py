# Generated by Django 3.0.6 on 2020-05-31 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0021_auto_20200531_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secciones',
            name='finaliza',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 9, 42, 31, 590911)),
        ),
    ]
