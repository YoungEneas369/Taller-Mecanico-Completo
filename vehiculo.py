# Clase que representa el molde para los vehículos del taller
class Vehiculo:
    # Método constructor que inicializa los atributos del vehículo
    def __init__(self, patente: str, anio: int) -> None:
        # Asigna la patente a través del setter de la propiedad para activar la validación
        self.patente = patente
        # Atributo privado para guardar el año del vehículo (con doble guion bajo)
        self.__anio = anio
        # Atributo privado para controlar el estado del vehículo en el taller (con doble guion bajo)
        self.__en_taller = False

    # El decorador @property transforma este método en una propiedad de lectura (getter) para patente
    @property
    def patente(self) -> str:
        # Retorna el valor guardado en el atributo privado __patente
        return self.__patente

    # El decorador @patente.setter define la propiedad de escritura (setter) con validación
    @patente.setter
    def patente(self, valor: str) -> None:
        # Valida que el texto de la patente tenga al menos 6 caracteres
        if len(valor) < 6:
            # Lanza una excepción ValueError si no cumple con el largo mínimo
            raise ValueError("La patente debe tener al menos 6 caracteres.")
        # Valida que el texto de la patente no contenga espacios en blanco
        if ' ' in valor:
            # Lanza una excepción ValueError si la patente contiene espacios
            raise ValueError("La patente no puede contener espacios.")
        # Si supera ambas validaciones, guarda el valor en el atributo privado __patente
        self.__patente = valor

    # El decorador @property transforma este método en una propiedad de lectura (getter) para anio
    @property
    def anio(self) -> int:
        # Retorna el valor guardado en el atributo privado __anio
        return self.__anio

    # El decorador @property define una propiedad de SOLO LECTURA para en_taller (sin setter asociado)
    @property
    def en_taller(self) -> bool:
        # Retorna el valor guardado en el atributo privado __en_taller
        return self.__en_taller

    # Método público para registrar el ingreso del vehículo al taller
    def ingresar(self) -> None:
        # Valida si el vehículo ya se encuentra actualmente dentro del taller
        if self.__en_taller:
            # Lanza un error ValueError si se intenta ingresar un vehículo que ya está en el taller
            raise ValueError("El vehículo ya se encuentra en el taller.")
        # Modifica directamente el atributo privado __en_taller a True si no estaba en el taller
        self.__en_taller = True

    # Método público para registrar la entrega del vehículo saliendo del taller
    def entregar(self) -> None:
        # Valida si el vehículo NO se encuentra actualmente dentro del taller
        if not self.__en_taller:
            # Lanza un error ValueError si se intenta entregar un vehículo que no está en el taller
            raise ValueError("El vehículo no está en el taller.")
        # Modifica directamente el atributo privado __en_taller a False si estaba en el taller
        self.__en_taller = False

    # Método que retorna el valor de la tarifa por hora de reparación básica
    def tarifa_hora(self) -> int:
        # Retorna el entero 5000 correspondiente a la tarifa por hora base
        return 5000
