# Importación de la clase base Vehiculo desde vehiculo.py
from vehiculo import Vehiculo

# Clase Auto que hereda de la clase base Vehiculo
class Auto(Vehiculo):
    # Sobrescribe el método tarifa_hora() de Vehiculo para especificar la tarifa propia de un Auto
    def tarifa_hora(self) -> int:
        # Retorna el número entero 25000 correspondiente a la tarifa por hora de reparación de un Auto
        return 25000
