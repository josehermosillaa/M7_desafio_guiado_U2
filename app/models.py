from django.db import models

# Create your models here.

"""
pk patente char(6) # CharField
marca char(20) not null # 
modelo char(20) not null#
year int not null # no puede ser negativo, mayor a cierto
"""

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    activo = models.BooleanField(default=False)

    creacion_registro = models.DateField(auto_now_add=True)
    
    #created_at
    #updated_at

    def __str__(self):
        return f"{self.marca} {self.modelo} : {self.patente}"


class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    vehiculo_id = models.OneToOneField('Vehiculo', related_name='chofer',on_delete=models.PROTECT)
    """
    debemos entender que si vehiculo_id en si es el objeto vehiculo completo,
    el cual necesitamos para generar un Chofer.
    Si queremos generar un chofer sin tener que pasar un vehiculo obligatoriamente,
    vehiculo_id = models.OneToOneField('Vehiculo', related_name='chofer',null=True, blank=True,on_delete=models.PROTECT)
    """
    creacion_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.rut} {self.nombre} : {self.apellido}"

class RegistroContabilidad(models.Model):
    fecha_compra = models.DateField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False) # como es un valor deberia ser siempre mayor que cero
    vehiculo_id = models.OneToOneField('Vehiculo', related_name='contabilidad',on_delete=models.PROTECT)
    creacion_registro = models.DateField(auto_now_add=True)




"""
OneToOneField --> ForeignKey + unique

foreign key se usa para uno es a muchos

onetone es para uno es a uno
"""