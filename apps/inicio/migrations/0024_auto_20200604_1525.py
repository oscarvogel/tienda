# Generated by Django 3.0.6 on 2020-06-04 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0023_auto_20200531_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secciones',
            name='finaliza',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 4, 15, 24, 59, 581995)),
        ),
    ]
