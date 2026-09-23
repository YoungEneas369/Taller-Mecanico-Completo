# Importación de la clase Vehiculo desde el módulo vehiculo.py
from vehiculo import Vehiculo

# Instanciación del primer vehículo v1 con patente 'KXPR84' y año 2019
v1 = Vehiculo('KXPR84', 2019)
# Instanciación del segundo vehículo v2 con patente 'JKLM12' y año 2016
v2 = Vehiculo('JKLM12', 2016)

# Registra la entrada al taller únicamente para el vehículo v1
v1.ingresar()

# Imprime la patente del primer vehículo v1 mediante la propiedad @property patente
print(f"Vehículo 1 - Patente: {v1.patente}")
# Imprime si v1 está en el taller mediante la propiedad @property en_taller (debe ser True)
print(f"Vehículo 1 - ¿Está en el taller?: {v1.en_taller}")

# Imprime la patente del segundo vehículo v2 mediante la propiedad @property patente
print(f"Vehículo 2 - Patente: {v2.patente}")
# Imprime si v2 está en el taller mediante la propiedad @property en_taller (debe ser False)
print(f"Vehículo 2 - ¿Está en el taller?: {v2.en_taller}")
