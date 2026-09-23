# Clase que representa el molde para los vehículos del taller
class Vehiculo:
    # Método constructor que inicializa los atributos privados del vehículo
    def __init__(self, patente: str, anio: int) -> None:
        # Atributo privado para guardar la patente del vehículo (con doble guion bajo)
        self.__patente = patente
        # Atributo privado para guardar el año del vehículo (con doble guion bajo)
        self.__anio = anio
        # Atributo privado para controlar el estado del vehículo en el taller (con doble guion bajo)
        self.__en_taller = False

    # Método público getter para obtener la patente del vehículo
    def obtener_patente(self) -> str:
        # Retorna el valor guardado en el atributo privado __patente
        return self.__patente

    # Método público getter para obtener el año del vehículo
    def obtener_anio(self) -> int:
        # Retorna el valor guardado en el atributo privado __anio
        return self.__anio

    # Método público getter para verificar si el vehículo está en el taller
    def esta_en_taller(self) -> bool:
        # Retorna el valor guardado en el atributo privado __en_taller
        return self.__en_taller

    # Método público para registrar el ingreso del vehículo al taller
    def ingresar(self) -> None:
        # Cambia el estado del atributo privado __en_taller a True
        self.__en_taller = True

    # Método público para registrar la entrega del vehículo saliendo del taller
    def entregar(self) -> None:
        # Cambia el estado del atributo privado __en_taller a False
        self.__en_taller = False
