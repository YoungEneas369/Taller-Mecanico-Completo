# Importación de la clase base Vehiculo desde vehiculo.py
from vehiculo import Vehiculo
# Importación de las nuevas subclases derivadas desde sus respectivos archivos
from auto import Auto
from moto import Moto
from camion import Camion

# Instanciación del primer vehículo v1 (Auto) con patente 'KXPR84' y año 2019
v1 = Auto('KXPR84', 2019)
# Instanciación del segundo vehículo v2 (Moto) con patente 'JKLM12' y año 2016
v2 = Moto('JKLM12', 2016)
# Instanciación de un camión con patente 'XYZ987' y año 2015
v3 = Camion('XYZ987', 2015)

# Registra la entrada al taller únicamente para el auto v1
v1.ingresar()

# Imprime la información del Auto v1 mediante la herencia de Vehiculo
print(f"Auto 1 - Patente: {v1.patente}, ¿En taller?: {v1.en_taller}, Tarifa hora: ${v1.tarifa_hora()}")

# Imprime la información de la Moto v2 mediante la herencia de Vehiculo
print(f"Moto 2 - Patente: {v2.patente}, ¿En taller?: {v2.en_taller}, Tarifa hora: ${v2.tarifa_hora()}")

# Imprime la información del Camión v3 mediante la herencia de Vehiculo
print(f"Camión 3 - Patente: {v3.patente}, ¿En taller?: {v3.en_taller}, Tarifa hora: ${v3.tarifa_hora()}")
