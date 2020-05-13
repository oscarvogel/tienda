from datetime import datetime

from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from django_mysql.models import Bit1BooleanField


class Localidades(models.Model):
    idlocalidad = models.AutoField(db_column='idLocalidad', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    nacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'localidades'
        verbose_name_plural = "Localidades"


class Tiporesp(models.Model):
    idtiporesp = models.AutoField(db_column='idTipoResp', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=40)  # Field name made lowercase.
    discrimina = models.TextField(db_column='Discrimina')  # Field name made lowercase. This field type is a guess.
    tipoiva = models.CharField(db_column='TipoIVA', max_length=1)  # Field name made lowercase.
    obligacuit = models.TextField(db_column='ObligaCUIT')  # Field name made lowercase. This field type is a guess.
    factura = models.PositiveIntegerField(db_column='Factura')  # Field name made lowercase.
    notacredito = models.PositiveIntegerField(db_column='NotaCredito')  # Field name made lowercase.
    notadebito = models.PositiveIntegerField(db_column='NotaDebito')  # Field name made lowercase.
    tipoivaepson = models.CharField(db_column='TipoIVaEpson', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiporesp'


class Grupos(models.Model):
    idgrupo = models.AutoField(db_column='idGrupo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=12, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grupos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Proveedores(models.Model):
    idproveedor = models.AutoField(db_column='idProveedor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    domicilio = models.CharField(db_column='Domicilio', max_length=50)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=50)  # Field name made lowercase.
    cuit = models.CharField(max_length=13)
    tiporesp = models.ForeignKey('Tiporesp', models.DO_NOTHING, db_column='TipoResp')  # Field name made lowercase.
    idlocalidad = models.ForeignKey('Localidades', models.DO_NOTHING, db_column='idLocalidad')  # Field name made lowercase.
    flete = models.DecimalField(max_digits=6, decimal_places=2)
    rentas = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'proveedores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Tipoiva(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=2)  # Field name made lowercase.
    descrip = models.CharField(db_column='DESCRIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='IVA', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    alicuota = models.DecimalField(db_column='ALICUOTA', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    percep = models.DecimalField(db_column='PERCEP', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoiva'

    def __str__(self):
        return self.descrip

class Marcas(models.Model):
    idmarca = models.AutoField(db_column='idMarca', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'marcas'
        ordering = ['nombre']
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nombre

class Talles(models.Model):
    idtalle = models.AutoField(db_column='idTalle', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'talles'
        ordering = ['nombre']
        verbose_name_plural = 'Talles'

    def __str__(self):
        return self.nombre

class Color(models.Model):
    idcolor = models.AutoField(db_column='idColor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    color = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'color'
        ordering = ['nombre']
        verbose_name_plural = 'Colores'

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    idarticulo = models.AutoField(db_column='idArticulo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    descripcion = models.TextField(default='', blank=True)
    nombreticket = models.CharField(db_column='NombreTicket', max_length=40)  # Field name made lowercase.
    idgrupo = models.ForeignKey('Grupos', models.DO_NOTHING, db_column='idGrupo',
                                verbose_name='Grupo')  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=12, decimal_places=2, default=0)  # Field name made lowercase.
    provppal = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='ProvPpal',
                                 verbose_name='Proveedor principal')  # Field name made lowercase.
    descstock = Bit1BooleanField(db_column='DescStock', verbose_name='Descuenta Stock', default=True)  # Field name made lowercase. This field type is a guess.
    tipoiva = models.ForeignKey('Tipoiva', models.DO_NOTHING, db_column='TipoIva', default='01')  # Field name made lowercase.
    idmarca = models.ForeignKey('Marcas', models.DO_NOTHING, db_column='idMarca', default=1)  # Field name made lowercase.
    preciopub = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    disponible_web = Bit1BooleanField(default=True, verbose_name = "Disponible venta web")

    class Meta:
        managed = False
        db_table = 'articulos'
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.nombre

class Stock(models.Model):
    idstock = models.AutoField(db_column='idStock', primary_key=True)  # Field name made lowercase.
    idarticulo = models.ForeignKey('Articulos', models.DO_NOTHING, db_column='idArticulo')  # Field name made lowercase.
    # idmarca = models.ForeignKey('Marcas', models.DO_NOTHING, db_column='idMarca', default=1, verbose_name='Marca')  # Field name made lowercase.
    idtalle = models.ForeignKey('Talles', models.DO_NOTHING, db_column='idTalle', verbose_name='Talle')  # Field name made lowercase.
    idcolorp = models.ForeignKey('Color', models.DO_NOTHING, db_column='idColorP', default=1, related_name='colorp')  # Field name made lowercase.
    idcolor = models.ForeignKey('Color', models.DO_NOTHING,db_column='idColorS', related_name='colors')  # Field name made lowercase.
    # costo = models.DecimalField(db_column='Costo', max_digits=12, decimal_places=2, default=0)  # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=12, decimal_places=4, default=0)  # Field name made lowercase.
    # stockminimo = models.DecimalField(db_column='StockMinimo', max_digits=12, decimal_places=4, default=0)  # Field name made lowercase.
    # incre1 = models.DecimalField(db_column='Incre1', max_digits=12, decimal_places=2, default=0)  # Field name made lowercase.
    # precio1 = models.DecimalField(db_column='Precio1', max_digits=12, decimal_places=2, default=0)  # Field name made lowercase.
    # incre2 = models.DecimalField(db_column='Incre2', max_digits=12, decimal_places=2, default=0)  # Field name made lowercase.
    # precio2 = models.DecimalField(db_column='Precio2', max_digits=12, decimal_places=2, default=0)  # Field name made lowercase.
    # incre3 = models.DecimalField(db_column='Incre3', max_digits=12, decimal_places=2, default=0)  # Field name made lowercase.
    # precio3 = models.DecimalField(db_column='Precio3', max_digits=12, decimal_places=2, default=0)  # Field name made lowercase.
    # visible = Bit1BooleanField(db_column='Visible', default=True)  # Field name made lowercase. This field type is a guess.
    descuenta = Bit1BooleanField(db_column='Descuenta', default=True)  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=20, default='')  # Field name made lowercase.
    # descstock = Bit1BooleanField(db_column='DescStock', default=True)  # Field name made lowercase. This field type is a guess.
    codbarraart = models.CharField(db_column='CodBarraArt', max_length=20, default='')  # Field name made lowercase.
    codbarrabulto = models.CharField(db_column='CodBarraBulto', max_length=20, default='')  # Field name made lowercase.
    # modificaprecios = Bit1BooleanField(db_column='ModificaPrecios', default=True)  # Field name made lowercase. This field type is a guess.
    imagen = models.CharField(db_column='Imagen', max_length=200, default='')  # Field name made lowercase.
    ultact = models.DateField(db_column='UltAct', default=datetime.now().date())  # Field name made lowercase.
    preciopub = models.DecimalField(db_column='PrecioPub', max_digits=12, decimal_places=4, default=0)  # Field name made lowercase.
    # balanza = Bit1BooleanField(db_column='Balanza', default=True)  # Field name made lowercase. This field type is a guess.
    plu = models.IntegerField(db_column='PLU', default=0)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=8, default='UN')  # Field name made lowercase.
    iddivisa = models.PositiveIntegerField(default=1)
    peso = models.DecimalField(db_column='Peso', max_digits=12, decimal_places=2, default=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock'
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'

    def __str__(self):
        return str(self.idstock)

class ImagenArticulo(models.Model):
    producto = models.ForeignKey(Articulos, models.DO_NOTHING)
    imagen = models.ImageField(upload_to='articulos/', blank=True)

    class Meta:
        verbose_name = 'Imagen Articulo'
        verbose_name_plural = 'Imagenes Articulo'

    def imagen_tag(self):
        return mark_safe('<img src="{}" width="50%" height="50%" />'.format(self.imagen.url))

    imagen_tag.short_description = 'Imagen'