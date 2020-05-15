from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from apps.productos.models import Articulos


class Paramsist(models.Model):
    idparamsist = models.AutoField(db_column='idParamSist', primary_key=True)  # Field name made lowercase.
    parametro = models.CharField(db_column='Parametro', max_length=100)  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=100)  # Field name made lowercase.
    detalle = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'paramsist'
        verbose_name = 'Parametros de sistema'
        verbose_name_plural = 'Parametros de sistema'

    def __str__(self):
        return self.parametro

    @classmethod
    def ObtenerValor(cls, valor_buscado=''):
        try:
            retorno = Paramsist.objects.get(parametro=valor_buscado)
            retorno = retorno.valor
        except:
            retorno = ''

        return retorno
    
class Secciones(models.Model):
    TIPO_SECCION = (
        ('B2', 'Banner principal'),
        ('S1', 'Seccion Uno'),
        ('S2', 'Seccion Dos'),
    )
    nombre = models.CharField(max_length=100, default='')
    tipo_seccion = models.CharField(max_length=2, default='', choices=TIPO_SECCION)
    descripcion = models.TextField(default='', blank=True)
    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)
    template = models.CharField(default='', max_length=200)
    imagen = models.ImageField(upload_to='portadas/', blank=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Seccion'
        verbose_name_plural = 'Secciones'

    def __str__(self):
        return self.nombre

    def imagen_tag(self):
        return mark_safe('<img src="{}" width="50%" height="50%" />'.format(self.imagen.url))

    imagen_tag.short_description = 'Imagen'

class DetalleSecciones(models.Model):

    seccion = models.ForeignKey(Secciones, models.DO_NOTHING)
    titulo = models.CharField(max_length=100, default='')
    detalle = models.TextField(default='', blank=True)
    articulo = models.ForeignKey(Articulos, models.DO_NOTHING, db_column='articulo')
    imagen = models.ImageField(upload_to='portadas/', blank=True)

    class Meta:
        verbose_name = 'Detalle Secciones'
        verbose_name_plural = 'Detalle Secciones'

    def imagen_tag(self):
        return mark_safe('<img src="{}" width="50%" height="50%" />'.format(self.imagen.url))

    imagen_tag.short_description = 'Imagen'