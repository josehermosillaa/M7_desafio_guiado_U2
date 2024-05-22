"""
● crear_vehiculo *
● crear_chofer *
● crear_registro_contable *
● deshabilitar_chofer *
● deshabilitar_vehiculo *
● habilitar_chofer *
● habilitar_vehiculo *
● obtener_vehiculo *
● obtener_chofer *

● imprimir_datos_vehiculos




● asignar_chofer_a_vehiculo -> se hace al crearlo

"""
from .models import Vehiculo, Chofer, RegistroContabilidad

def crear_vehiculo(patente, marca,modelo,year,activo):
    vehiculo = Vehiculo(
        patente=patente,
        marca=marca,
        modelo=modelo,
        year=year,
        activo=activo
        )
    vehiculo.full_clean() # aplica las condiciones del modelo
    vehiculo.save()

    return vehiculo

def obtener_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    return vehiculo

def crear_chofer(rut, nombre,apellido,activo,vehiculo_id):
    vehiculo = obtener_vehiculo(vehiculo_id)
    chofer = Chofer(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=activo,
        vehiculo_id=vehiculo
    )
    chofer.save()
    return chofer

def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    return chofer

def crear_registro_contable(fecha_compra,valor,vehiculo_id):
    vehiculo = Vehiculo.objects.get(patente=vehiculo_id)
    registro = RegistroContabilidad(
        fecha_compra=fecha_compra,
        valor=valor,
        vehiculo_id=vehiculo
    )
    registro.save()
    return registro


""" por aqui puede entrar el rut de un chofer
o el objeto chofer.
supondremos que entra el objeto chofer


chofer es un objeto Chofer!
parametro ->activo

en el caso que se pase el rut como argumento

def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()
    return chofer

*asumiremos lo mismo para los vehiculos *


"""
def deshabilitar_chofer(chofer):
    chofer.activo = False
    chofer.save()
    return chofer

def habilitar_chofer(chofer):
    chofer.activo = True
    chofer.save()
    return chofer

def deshabilitar_vehiculo(vehiculo):
    vehiculo.activo = False
    vehiculo.save()
    return vehiculo

def habilitar_vehiculo(vehiculo):
    vehiculo.activo = True
    vehiculo.save()
    return vehiculo

#se espera toda la informacion de los vehiculos

def imprimir_vehiculos():
    vehiculos = Vehiculo.objects.all()

    for v in vehiculos:
        print(f""" Vehiculo:{v.patente}/{v.marca}/{v.modelo}/{v.year}/activo:{v.activo}""")

        if hasattr(v, 'chofer'):
            print(f"""  Chofer[{v.chofer.rut}]: {v.chofer.nombre} {v.chofer.apellido}/ activo: {v.chofer.activo}""")
        if hasattr(v,'contabilidad'):
            print(f"""  Contabilidad:[{v.contabilidad.id}]: fecha_compra:{v.contabilidad.fecha_compra}/valor:{v.contabilidad.valor}""")
        print("\n")