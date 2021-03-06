# Generated by Django 3.0.6 on 2020-05-25 09:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0013_auto_20200523_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 9, 13, 45, 384631)),
        ),
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2020, 5, 25, 9, 13, 45, 387629))),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='productos.Articulos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Favoritos',
                'verbose_name_plural': 'Favoritos',
            },
        ),
    ]
