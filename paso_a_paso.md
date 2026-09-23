# Paso a Paso del Proyecto: Taller Mecánico Completo

Guía paso a paso del desarrollo del proyecto para el módulo **Programación Orientada a Objetos Seguro** (2° Semestre 2026).

---

## Historial de Pasos y Evolución del Proyecto

### Paso 1: Configuración Inicial del Repositorio
- Creación del repositorio `Taller-Mecanico-Completo` en GitHub.
- Clonación en la carpeta `Documentos`.
- Creación de ramas `main`, `master` y `feature/desarrollo`.
- Creación del archivo `README.md` inicial.

---

### Paso 2: Creación de la Clase Vehículo
- Creación del archivo `vehiculo.py`.
- Definición de la estructura básica del molde de la clase `Vehiculo`.

---

### Paso 3: Declaración de Atributos en la Clase Vehículo
- Definición de atributos con anotación de tipos en `Vehiculo`: `patente: str`, `anio: int`, `_en_taller: bool`.

---

### Paso 4: Implementación del Constructor `__init__`
- Creación del constructor en `Vehiculo` recibiendo `patente` y `anio`.
- Asignación fija de `_en_taller = False` al instanciar (ya que un vehículo recién registrado nunca ingresa directamente en el taller).
- Documentación y comentarios explicativos por cada línea de código.

---

### Paso 5: Creación del Punto de Entrada `main.py`
- Importación de la clase `Vehiculo` desde `vehiculo.py`.
- Instanciación de un objeto `Vehiculo` con patente `'KXPR84'` y año `2019`.
- Impresión en consola de los atributos `patente`, `anio` y `_en_taller`.

---

### Paso 6: Métodos `ingresar()` y `entregar()` en la Clase `Vehiculo`
- Implementación del método `ingresar()` que cambia `_en_taller` a `True`.
- Implementación del método `entregar()` que cambia `_en_taller` a `False`.
- Modificación de `main.py` para probar la transición de estados (`False` -> `True` -> `False`).

---

### Paso 7: Creación de `linea_detalle.py` y Limpieza de Atributos Fuera del Constructor
- Creación de `linea_detalle.py` con la clase `LineaDetalle`.
- Implementación del constructor con `cantidad` y `precio_unitario`.
- Implementación del método `subtotal()` que retorna `cantidad * precio_unitario`.
- Remoción de declaraciones de atributos fuera del constructor en `vehiculo.py`.

---

### Paso 8: Encapsulamiento con Métodos Getters Tradicionales
- Conversión de atributos a privados usando doble guion bajo (`__patente`, `__anio`, `__en_taller`).
- Creación de métodos getters tradicionales: `obtener_patente()`, `obtener_anio()`, `esta_en_taller()`.

---

### Paso 9: Reemplazo por `@property` (Getters Pythonicos)
- Reemplazo de métodos `obtener_patente()`, `obtener_anio()` y `esta_en_taller()` por las propiedades `@property` asociadas: `patente`, `anio` y `en_taller`.
- Explicación de cómo `@property` permite acceder a atributos privados utilizando la sintaxis de atributos sin paréntesis `()`.

---

### Paso 10: Prueba de Instancias Independientes `v1` y `v2` en `main.py`
- Creación de dos instancias independientes: `v1` (`'KXPR84'`, `2019`) y `v2` (`'JKLM12'`, `2016`).
- Llamada a `v1.ingresar()` únicamente en `v1`.
- Verificación mediante impresiones que `v1.en_taller` cambia a `True`, mientras que `v2.en_taller` se mantiene en `False`.

---

### Paso 11: Método `tarifa_hora()` en la Clase `Vehiculo`
- Implementación del método `tarifa_hora()` en `Vehiculo` que retorna el entero `5000`.

---

### Paso 12: Herencia - Subclases `Auto`, `Moto` y `Camion`
- Creación de los módulos `auto.py`, `moto.py` y `camion.py`.
- Definición de las subclases `Auto`, `Moto` y `Camion` heredando de `Vehiculo` (`class NombreClase(Vehiculo): pass`).
- Actualización de `main.py` importando e instanciando las tres subclases para comprobar la herencia.
