# Generated by Django 3.0.6 on 2020-05-17 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20200514_1931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupos',
            options={'managed': False, 'ordering': ['nombre'], 'verbose_name': 'Grupo', 'verbose_name_plural': 'Grupos'},
        ),
    ]
