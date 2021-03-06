# Generated by Django 3.0.6 on 2020-05-17 12:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150)),
                ('created', models.DateTimeField(default=datetime.datetime(2020, 5, 17, 12, 53, 9, 917158))),
                ('updated', models.DateTimeField(default=datetime.datetime(2020, 5, 17, 12, 53, 9, 917158))),
                ('state', models.CharField(choices=[('P', 'Publicado'), ('B', 'Borrador'), ('A', 'Anulado')], max_length=1)),
                ('image', models.ImageField(blank=True, upload_to='blog/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
                'ordering': ['-created_by'],
            },
        ),
        migrations.CreateModel(
            name='BlogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog')),
            ],
            options={
                'verbose_name': 'Detalle Blog',
                'verbose_name_plural': 'Detalle Blog',
            },
        ),
    ]
