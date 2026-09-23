# Importación de la clase Vehiculo desde el módulo vehiculo.py
from vehiculo import Vehiculo

# Creación de una instancia de Vehiculo con patente 'KXPR84' y año 2019
mi_vehiculo = Vehiculo('KXPR84', 2019)

# Muestra de los atributos del vehículo por consola
print(f"Patente: {mi_vehiculo.patente}")
print(f"Año: {mi_vehiculo.anio}")
print(f"¿Está en el taller?: {mi_vehiculo._en_taller}")
