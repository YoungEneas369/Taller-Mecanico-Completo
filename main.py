# Importación de la clase Vehiculo desde el módulo vehiculo.py
from vehiculo import Vehiculo

# Creación de una instancia de Vehiculo con patente 'KXPR84' y año 2019
mi_vehiculo = Vehiculo('KXPR84', 2019)

# Muestra la información básica del vehículo instanciado
print(f"Patente: {mi_vehiculo.patente}")
# Muestra el año del vehículo instanciado
print(f"Año: {mi_vehiculo.anio}")
# Muestra el estado inicial del vehículo (debe ser False)
print(f"Estado inicial ¿está en el taller?: {mi_vehiculo._en_taller}")

# Ejecuta el método ingresar() para cambiar el estado del vehículo a dentro del taller
mi_vehiculo.ingresar()
# Muestra el estado del vehículo luego de llamar a ingresar() (debe ser True)
print(f"Estado tras llamar a ingresar() ¿está en el taller?: {mi_vehiculo._en_taller}")

# Ejecuta el método entregar() para cambiar el estado del vehículo a fuera del taller
mi_vehiculo.entregar()
# Muestra el estado del vehículo luego de llamar a entregar() (debe ser False)
print(f"Estado tras llamar a entregar() ¿está en el taller?: {mi_vehiculo._en_taller}")
