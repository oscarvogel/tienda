# Generated by Django 3.0.6 on 2020-05-27 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0018_auto_20200527_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secciones',
            name='finaliza',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 27, 16, 29, 1, 292583)),
        ),
    ]
