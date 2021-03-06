# Generated by Django 3.0.6 on 2020-08-19 15:48

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200604_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 15, 48, 20, 988671), verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 15, 48, 20, 988671), verbose_name='Actualizado'),
        ),
        migrations.AlterField(
            model_name='blogdetail',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
