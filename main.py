# Importación de la clase Vehiculo desde el módulo vehiculo.py
from vehiculo import Vehiculo

# Creación de una instancia de Vehiculo con patente 'KXPR84' y año 2019
mi_vehiculo = Vehiculo('KXPR84', 2019)

# Muestra la patente del vehículo usando el getter público obtener_patente()
print(f"Patente: {mi_vehiculo.obtener_patente()}")
# Muestra el año del vehículo usando el getter público obtener_anio()
print(f"Año: {mi_vehiculo.obtener_anio()}")
# Muestra el estado inicial del vehículo usando el getter público esta_en_taller()
print(f"Estado inicial ¿está en el taller?: {mi_vehiculo.esta_en_taller()}")

# Ejecuta el método ingresar() para cambiar el estado del vehículo a dentro del taller
mi_vehiculo.ingresar()
# Muestra el estado del vehículo luego de llamar a ingresar() usando esta_en_taller()
print(f"Estado tras llamar a ingresar() ¿está en el taller?: {mi_vehiculo.esta_en_taller()}")

# Ejecuta el método entregar() para cambiar el estado del vehículo a fuera del taller
mi_vehiculo.entregar()
# Muestra el estado del vehículo luego de llamar a entregar() usando esta_en_taller()
print(f"Estado tras llamar a entregar() ¿está en el taller?: {mi_vehiculo.esta_en_taller()}")
