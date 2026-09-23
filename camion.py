# Importación de la clase base Vehiculo desde vehiculo.py
from vehiculo import Vehiculo

# Clase Camion que hereda de la clase base Vehiculo
class Camion(Vehiculo):
    # Método constructor propio que recibe patente, anio y capacidad_carga como parámetros
    def __init__(self, patente: str, anio: int, capacidad_carga: int) -> None:
        # Llama al constructor de la superclase Vehiculo para guardar patente y anio
        super().__init__(patente, anio)
        # Guarda la capacidad de carga en kilos en el atributo privado __capacidad_carga
        self.__capacidad_carga = capacidad_carga

    # El decorador @property define una propiedad de lectura (getter) para capacidad_carga
    @property
    def capacidad_carga(self) -> int:
        # Retorna el valor almacenado en el atributo privado __capacidad_carga
        return self.__capacidad_carga
