# Generated by Django 3.0.6 on 2020-05-17 13:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20200517_1012'),
        ('inicio', '0006_secciones_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='secciones',
            name='finaliza',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 10, 12, 20, 17280)),
        ),
        migrations.AlterField(
            model_name='detallesecciones',
            name='articulo',
            field=models.ForeignKey(db_column='articulo', on_delete=django.db.models.deletion.DO_NOTHING, to='productos.Articulos'),
        ),
        migrations.AlterField(
            model_name='secciones',
            name='tipo_seccion',
            field=models.CharField(choices=[('B2', 'Banner principal'), ('S1', 'Seccion Uno'), ('S2', 'Seccion Dos'), ('OF', 'Seccion de ofertas')], default='', max_length=2),
        ),
    ]
