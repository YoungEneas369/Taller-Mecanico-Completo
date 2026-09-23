# Clase que representa el molde básico para los vehículos del taller
class Vehiculo:
    # Declaración del atributo patente de tipo texto (cadena de caracteres)
    patente: str
    # Declaración del atributo anio de tipo número entero
    anio: int
    # Declaración del atributo _en_taller de tipo booleano (verdadero o falso)
    _en_taller: bool

    # Método constructor que inicializa los atributos del vehículo al crear la instancia
    def __init__(self, patente: str, anio: int) -> None:
        # Guarda el parámetro patente recibido en el atributo de la instancia
        self.patente = patente
        # Guarda el parámetro anio recibido en el atributo de la instancia
        self.anio = anio
        # Establece _en_taller por defecto en False, indicando que el vehículo no inicia en el taller
        self._en_taller = False
