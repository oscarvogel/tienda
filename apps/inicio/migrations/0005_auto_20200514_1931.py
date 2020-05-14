# Generated by Django 3.0.6 on 2020-05-14 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_secciones_orden'),
    ]

    operations = [
        migrations.AddField(
            model_name='secciones',
            name='template',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='secciones',
            name='tipo_seccion',
            field=models.CharField(choices=[('B2', 'Banner principal'), ('S1', 'Seccion Uno'), ('S2', 'Seccion Dos')], default='', max_length=2),
        ),
    ]
