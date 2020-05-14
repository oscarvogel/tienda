# Generated by Django 3.0.6 on 2020-05-13 18:54

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models.fields.bit


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('idarticulo', models.AutoField(db_column='idArticulo', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=100)),
                ('descripcion', models.TextField(blank=True, default='')),
                ('nombreticket', models.CharField(db_column='NombreTicket', max_length=40)),
                ('peso', models.DecimalField(db_column='Peso', decimal_places=2, max_digits=12)),
                ('descstock', django_mysql.models.fields.bit.Bit1BooleanField(db_column='DescStock', verbose_name='Descuenta Stock')),
                ('preciopub', models.DecimalField(decimal_places=2, max_digits=12)),
                ('disponible_web', django_mysql.models.fields.bit.Bit1BooleanField(default=0, verbose_name='Disponible venta web')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
                'db_table': 'articulos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('idcolor', models.AutoField(db_column='idColor', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=100)),
                ('color', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'color',
                'ordering': ['nombre'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('idgrupo', models.AutoField(db_column='idGrupo', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('porcentaje', models.DecimalField(db_column='Porcentaje', decimal_places=2, max_digits=12)),
            ],
            options={
                'db_table': 'grupos',
                'ordering': ['nombre'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('idlocalidad', models.AutoField(db_column='idLocalidad', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('nacion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'localidades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('idmarca', models.AutoField(db_column='idMarca', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'marcas',
                'ordering': ['nombre'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('idproveedor', models.AutoField(db_column='idProveedor', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('domicilio', models.CharField(db_column='Domicilio', max_length=50)),
                ('telefono', models.CharField(db_column='Telefono', max_length=50)),
                ('cuit', models.CharField(max_length=13)),
                ('flete', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rentas', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'proveedores',
                'ordering': ['nombre'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('idstock', models.AutoField(db_column='idStock', primary_key=True, serialize=False)),
                ('costo', models.DecimalField(db_column='Costo', decimal_places=2, max_digits=12)),
                ('stock', models.DecimalField(db_column='Stock', decimal_places=4, max_digits=12)),
                ('stockminimo', models.DecimalField(db_column='StockMinimo', decimal_places=4, max_digits=12)),
                ('incre1', models.DecimalField(db_column='Incre1', decimal_places=2, max_digits=12)),
                ('precio1', models.DecimalField(db_column='Precio1', decimal_places=2, max_digits=12)),
                ('incre2', models.DecimalField(db_column='Incre2', decimal_places=2, max_digits=12)),
                ('precio2', models.DecimalField(db_column='Precio2', decimal_places=2, max_digits=12)),
                ('incre3', models.DecimalField(db_column='Incre3', decimal_places=2, max_digits=12)),
                ('precio3', models.DecimalField(db_column='Precio3', decimal_places=2, max_digits=12)),
                ('visible', django_mysql.models.fields.bit.Bit1BooleanField(db_column='Visible')),
                ('descuenta', models.BooleanField(db_column='Descuenta')),
                ('formula', models.CharField(db_column='Formula', max_length=20)),
                ('descstock', models.TextField(db_column='DescStock')),
                ('codbarraart', models.CharField(db_column='CodBarraArt', max_length=20)),
                ('codbarrabulto', models.CharField(db_column='CodBarraBulto', max_length=20)),
                ('modificaprecios', django_mysql.models.fields.bit.Bit1BooleanField(db_column='ModificaPrecios')),
                ('imagen', models.CharField(db_column='Imagen', max_length=200)),
                ('ultact', models.DateField(db_column='UltAct')),
                ('preciopub', models.DecimalField(db_column='PrecioPub', decimal_places=4, max_digits=12)),
                ('balanza', models.TextField(db_column='Balanza')),
                ('plu', models.IntegerField(db_column='PLU')),
                ('unidad', models.CharField(db_column='Unidad', max_length=8)),
                ('iddivisa', models.PositiveIntegerField()),
                ('peso', models.DecimalField(db_column='Peso', decimal_places=2, max_digits=12)),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stock',
                'db_table': 'stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Talles',
            fields=[
                ('idtalle', models.AutoField(db_column='idTalle', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=100)),
            ],
            options={
                'db_table': 'talles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipoiva',
            fields=[
                ('codigo', models.CharField(db_column='CODIGO', max_length=2, primary_key=True, serialize=False)),
                ('descrip', models.CharField(blank=True, db_column='DESCRIP', max_length=20, null=True)),
                ('iva', models.DecimalField(blank=True, db_column='IVA', decimal_places=2, max_digits=5, null=True)),
                ('alicuota', models.DecimalField(blank=True, db_column='ALICUOTA', decimal_places=2, max_digits=5, null=True)),
                ('percep', models.DecimalField(blank=True, db_column='PERCEP', decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'db_table': 'tipoiva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiporesp',
            fields=[
                ('idtiporesp', models.AutoField(db_column='idTipoResp', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=40)),
                ('discrimina', models.TextField(db_column='Discrimina')),
                ('tipoiva', models.CharField(db_column='TipoIVA', max_length=1)),
                ('obligacuit', models.TextField(db_column='ObligaCUIT')),
                ('factura', models.PositiveIntegerField(db_column='Factura')),
                ('notacredito', models.PositiveIntegerField(db_column='NotaCredito')),
                ('notadebito', models.PositiveIntegerField(db_column='NotaDebito')),
                ('tipoivaepson', models.CharField(db_column='TipoIVaEpson', max_length=1)),
            ],
            options={
                'db_table': 'tiporesp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImagenArticulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, upload_to='articulos/%Y/%m/%d')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='productos.Articulos')),
            ],
            options={
                'verbose_name': 'Imagen Articulo',
                'verbose_name_plural': 'Imagenes Articulo',
            },
        ),
    ]
