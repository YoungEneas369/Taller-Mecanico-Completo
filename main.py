# Importación de la clase Vehiculo desde el módulo vehiculo.py
from vehiculo import Vehiculo

# Creación de una instancia de Vehiculo con patente 'KXPR84' y año 2019
mi_vehiculo = Vehiculo('KXPR84', 2019)

# Muestra la patente accediendo a la propiedad @property patente sin usar paréntesis ()
print(f"Patente: {mi_vehiculo.patente}")
# Muestra el año accediendo a la propiedad @property anio sin usar paréntesis ()
print(f"Año: {mi_vehiculo.anio}")
# Muestra el estado inicial accediendo a la propiedad @property en_taller sin usar paréntesis ()
print(f"Estado inicial ¿está en el taller?: {mi_vehiculo.en_taller}")

# Ejecuta el método ingresar() para cambiar el estado del vehículo a dentro del taller
mi_vehiculo.ingresar()
# Muestra el estado tras ingresar accediendo a la propiedad @property en_taller
print(f"Estado tras llamar a ingresar() ¿está en el taller?: {mi_vehiculo.en_taller}")

# Ejecuta el método entregar() para cambiar el estado del vehículo a fuera del taller
mi_vehiculo.entregar()
# Muestra el estado tras entregar accediendo a la propiedad @property en_taller
print(f"Estado tras llamar a entregar() ¿está en el taller?: {mi_vehiculo.en_taller}")
