from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

class Blog(models.Model):

    STATE_BLOG = (
        ('P', 'Publicado'),
        ('B', 'Borrador'),
        ('A', 'Anulado'),
    )
    title = models.CharField(max_length=150, default='', verbose_name='Titulo')
    created = models.DateTimeField(default=datetime.now(), verbose_name='Creado')
    updated = models.DateTimeField(default=datetime.now(), verbose_name='Actualizado')
    created_by = models.ForeignKey(User, models.DO_NOTHING, related_name='created_by', verbose_name='Creado por')
    updated_by = models.ForeignKey(User, models.DO_NOTHING, related_name='updated_by', verbose_name='Actualizado por')
    state = models.CharField(max_length=1, choices=STATE_BLOG, verbose_name='Estado')
    image = models.ImageField(upload_to='blog/', blank=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
        ordering = ['-created_by']

    def image_tag(self):
        return mark_safe('<img src="{}" width="50%" height="50%" />'.format(self.image.url))

    image_tag.short_description = 'Imagen'

    def __str__(self):
        return self.title


class BlogDetail(models.Model):

    blog = models.ForeignKey(Blog, models.DO_NOTHING)
    content = RichTextField(verbose_name='Contenido')

    class Meta:
        verbose_name = 'Detalle Blog'
        verbose_name_plural = 'Detalle Blog'