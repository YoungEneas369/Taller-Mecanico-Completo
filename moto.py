# Importación de la clase base Vehiculo desde vehiculo.py
from vehiculo import Vehiculo

# Clase Moto que hereda de la clase base Vehiculo
class Moto(Vehiculo):
    # Sobrescribe el método tarifa_hora() de Vehiculo para especificar la tarifa propia de una Moto
    def tarifa_hora(self) -> int:
        # Retorna el número entero 15000 correspondiente a la tarifa por hora de reparación de una Moto
        return 15000
