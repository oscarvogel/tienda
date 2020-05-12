# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Paramsist(models.Model):
    idparamsist = models.AutoField(db_column='idParamSist', primary_key=True)  # Field name made lowercase.
    parametro = models.CharField(db_column='Parametro', max_length=100)  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=100)  # Field name made lowercase.
    detalle = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'paramsist'
