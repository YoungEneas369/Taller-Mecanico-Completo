# Taller Mecánico Completo

Este repositorio contiene el desarrollo del modelo completo de un taller mecánico para el módulo **Programación Orientada a Objetos Seguro** del **segundo semestre del año 2026**.

---

## Bitácora de Commits / Evolución Histórica del Proyecto

A continuación se detalla la secuencia evolutiva de desarrollo del software, donde cada instrucción/prompt corresponde a un cambio y un commit independiente en el repositorio:

| Commit | Mensaje / Requerimiento | Archivos Modificados | Descripción del Cambio |
| :---: | :--- | :--- | :--- |
| `c8a26c3` | `feat: inicializar repositorio y agregar README.md base` | `README.md`, `.gitignore` | Inicialización del repositorio base con la información general del proyecto. |
| `fa8ac0a` | `feat: crear clase Vehiculo vacia en vehiculo.py` | `vehiculo.py` | Creación del archivo `vehiculo.py` con el molde inicial vacío de la clase `Vehiculo`. |
| `fae67f0` | `feat: agregar declaraciones de tipo para patente, anio y _en_taller` | `vehiculo.py` | Declaración de los atributos `patente`, `anio` y `_en_taller` con anotación de tipos. |
| `3511756` | `feat: agregar constructor __init__ con patente, anio y _en_taller=False` | `vehiculo.py` | Implementación del método constructor `__init__` inicializando `_en_taller` en `False`. |
| `e719f08` | `feat: crear main.py para instanciar Vehiculo e imprimir atributos` | `main.py` | Creación del punto de entrada `main.py` instanciando un objeto e imprimiendo sus datos. |
| `ff454e6` | `feat: agregar métodos ingresar() y entregar() en Vehiculo y probar en main.py` | `vehiculo.py`, `main.py` | Adición de los métodos `ingresar()` y `entregar()` y su correspondiente prueba en `main.py`. |
| `f534710` | `feat: crear clase LineaDetalle y eliminar variables de clase en vehiculo.py` | `linea_detalle.py`, `vehiculo.py` | Creación de la clase `LineaDetalle` con constructor y método `subtotal()`. Limpieza de atributos de clase. |
| `cbddcef` | `feat: privatizar atributos con __ y agregar getters obtener_patente, obtener_anio, esta_en_taller` | `vehiculo.py`, `main.py` | Encapsulamiento con atributos privados (`__patente`, `__anio`, `__en_taller`) y métodos getters tradicionales. |
| `790fdc6` | `refactor: reemplazar getters tradicionales por decoradores @property en Vehiculo` | `vehiculo.py`, `main.py` | Implementación del estilo pythonico usando decoradores `@property` (`patente`, `anio`, `en_taller`). |
| `c099d9d` | `test: instanciar v1 y v2 en main.py probando independencia de estados` | `main.py` | Prueba con dos vehículos (`v1` y `v2`) verificando la independencia del estado `en_taller`. |
| `d930fff` | `feat: agregar método tarifa_hora() en Vehiculo retornando 5000` | `vehiculo.py`, `main.py` | Método `tarifa_hora()` en `Vehiculo` retornando el número entero `5000` (tarifa por hora). |
| `a482f1b` | `docs: actualizar bitacora de commits con la tarifa_hora() y paso_a_paso.md` | `README.md`, `paso_a_paso.md` | Actualización de la bitácora de commits y del documento explicativo. |

---

## Estructura del Código Actual

- [`vehiculo.py`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/vehiculo.py): Clase `Vehiculo` encapsulada con `@property`, métodos `ingresar()`, `entregar()` y `tarifa_hora()`.
- [`linea_detalle.py`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/linea_detalle.py): Clase `LineaDetalle` con constructor y cálculo de `subtotal()`.
- [`main.py`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/main.py): Punto de entrada para pruebas con múltiples instancias de vehículos.
- [`paso_a_paso.md`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/paso_a_paso.md): Explicación pedagógica del avance del desarrollo.
