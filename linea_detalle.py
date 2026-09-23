# Clase que representa una línea de detalle en el taller
class LineaDetalle:
    # Método constructor que recibe la cantidad y el precio unitario
    def __init__(self, cantidad: int, precio_unitario: float) -> None:
        # Guarda la cantidad enviada como parámetro
        self.cantidad = cantidad
        # Guarda el precio unitario enviado como parámetro
        self.precio_unitario = precio_unitario

    # Método que calcula el subtotal de la línea de detalle
    def subtotal(self) -> float:
        # Retorna la multiplicación de la cantidad por el precio unitario
        return self.cantidad * self.precio_unitario
