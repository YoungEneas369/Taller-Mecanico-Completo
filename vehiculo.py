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

    # El decorador @property transforma este método en una propiedad de lectura (getter).
    # Permite acceder al valor de self.__patente como si fuera un atributo público (objeto.patente) sin usar paréntesis ().
    @property
    def patente(self) -> str:
        # Retorna el valor guardado en el atributo privado __patente
        return self.__patente

    # El decorador @property transforma este método en una propiedad de lectura (getter).
    # Permite acceder al valor de self.__anio como un atributo público (objeto.anio) manteniendo el atributo protegido/privado.
    @property
    def anio(self) -> int:
        # Retorna el valor guardado en el atributo privado __anio
        return self.__anio

    # El decorador @property transforma este método en una propiedad de lectura (getter).
    # Permite consultar si está en taller con sintaxis de atributo (objeto.en_taller) ejecutando este método internamente.
    @property
    def en_taller(self) -> bool:
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

    # Método que retorna el valor de la tarifa por hora de reparación para el vehículo
    def tarifa_hora(self) -> int:
        # Retorna el entero 5000 correspondiente a la tarifa por hora de reparación
        return 5000
