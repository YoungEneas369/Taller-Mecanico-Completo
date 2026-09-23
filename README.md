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
| `e1b48bc` | `feat: crear subclases Auto, Moto y Camion heredando de Vehiculo y actualizar main.py` | `auto.py`, `moto.py`, `camion.py`, `main.py` | Creación de subclases `Auto`, `Moto` y `Camion` heredando de `Vehiculo` y actualización de `main.py`. |
| `7aef6ee` | `feat: agregar constructor con super().__init__, atributo privado __capacidad_carga y getter en Camion` | `camion.py`, `main.py` | Constructor propio en `Camion` con `super().__init__()`, atributo privado `__capacidad_carga` y su getter `@property`. |
| `8625af5` | `feat: sobrescribir tarifa_hora() en Auto (25000), Moto (15000) y Camion (40000)` | `auto.py`, `moto.py`, `camion.py` | Polimorfismo: sobrescritura de `tarifa_hora()` retornando `25000` (Auto), `15000` (Moto) y `40000` (Camion). |
| `7a3c0b1` | `feat: agregar @patente.setter con validacion de longitud y espacios en Vehiculo` | `vehiculo.py` | Validación segura de la patente mediante `@patente.setter` lanzando `ValueError` y asignación en constructor. |
| `0e41b2c` | `docs: actualizar bitacora de commits con @patente.setter y paso_a_paso.md` | `README.md`, `paso_a_paso.md` | Actualización de la bitácora de commits y del documento explicativo. |

---

## Estructura del Código Actual

- [`vehiculo.py`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/vehiculo.py): Clase base `Vehiculo` con propiedad `@patente.setter` para validación segura.
- [`auto.py`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/auto.py): Subclase `Auto` (`tarifa_hora` = `25000`).
- [`moto.py`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/moto.py): Subclase `Moto` (`tarifa_hora` = `15000`).
- [`camion.py`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/camion.py): Subclase `Camion` (`tarifa_hora` = `40000`, `capacidad_carga`).
- [`linea_detalle.py`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/linea_detalle.py): Clase `LineaDetalle`.
- [`main.py`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/main.py): Punto de entrada instanciando subclases `Auto`, `Moto` y `Camion`.
- [`paso_a_paso.md`](file:///C:/Users/figue/Documents/Taller-Mecanico-Completo/paso_a_paso.md): Guía paso a paso del proyecto.
