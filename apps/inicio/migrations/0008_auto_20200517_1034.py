# Generated by Django 3.0.6 on 2020-05-17 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0007_auto_20200517_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secciones',
            name='finaliza',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 10, 34, 31, 502855)),
        ),
    ]
