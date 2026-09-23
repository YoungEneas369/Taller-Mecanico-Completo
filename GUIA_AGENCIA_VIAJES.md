# Guía Pedagógica y Lista de Prompts: Modelo Agencia de Viajes

Esta guía traslada el mismo enfoque evolutivo de la **Programación Orientada a Objetos Seguro** aplicado al taller mecánico hacia el dominio de una **Agencia de Viajes**. Puedes reutilizar cada uno de estos prompts secuencialmente en tus futuras clases.

---

## Mapeo de Conceptos: Taller Mecánico vs. Agencia de Viajes

| Concepto POO | Taller Mecánico | Agencia de Viajes |
| :--- | :--- | :--- |
| **Clase Base** | `Vehiculo` | `ServicioViaje` |
| **Atributos de Entidad** | `patente`, `anio`, `_en_taller` | `codigo`, `precio_base`, `_reservado` |
| **Métodos de Estado** | `ingresar()`, `entregar()` | `reservar()`, `cancelar()` |
| **Clase Auxiliar** | `LineaDetalle` | `Pasajero` / `Ticket` |
| **Subclases (Herencia)** | `Auto`, `Moto`, `Camion` | `Vuelo`, `Hotel`, `Excursion` |
| **Atributo Específico** | `capacidad_carga` (Camion) | `noches` (Hotel) |
| **Polimorfismo** | `tarifa_hora()` | `costo_total()` |
| **Validación Segura** | `@patente.setter` | `@codigo.setter` |

---

## Lista Secuencial de Prompts para la Agencia de Viajes

### Prompt 1: Repositorio e Inicialización
> *"Crea un repositorio vacío llamado Agencia-Viajes-Completo. Clónalo en la carpeta Documentos, inicialízalo con una rama main y crea un README.md que explique que crearemos el modelo completo de una agencia de viajes para el módulo POO Seguro."*

### Prompt 2: Clase Base Vacía
> *"Crea en servicio_viaje.py la clase ServicioViaje, vacía por ahora con pass, sin atributos ni métodos todavía. Agrega un comentario explicando que es solo el molde básico."*

### Prompt 3: Declaración de Atributos con Tipado
> *"Agrégale a la clase ServicioViaje los atributos codigo (texto), precio_base (número entero o flotante) y _reservado (verdadero o falso), con sus anotaciones de tipo indicadas, sin constructor todavía."*

### Prompt 4: Constructor `__init__`
> *"Agrégale a ServicioViaje un constructor __init__ que reciba codigo y precio_base como parámetros y los guarde. El atributo _reservado fijalo siempre en False por defecto, porque un servicio recién creado nunca parte reservado. Comenta cada línea."*

### Prompt 5: Punto de Entrada `main.py`
> *"Créame main.py: importa ServicioViaje desde servicio_viaje.py, crea un servicio con código 'VUE123' y precio base 150000, y usa print() para mostrar su código, precio y si está reservado."*

### Prompt 6: Métodos de Estado (`reservar` y `cancelar`)
> *"Agrégale a ServicioViaje los métodos reservar() y cancelar(): cambian _reservado a True o False según corresponda. Modifica main.py para probar estos métodos. Comenta cada línea."*

### Prompt 7: Clase Auxiliar y Limpieza
> *"Crea pasajero.py con la clase Pasajero: constructor que reciba nombre y rut, y un método datos_completos() que los retorne. Elimina cualquier declaración de variables de clase fuera del constructor en servicio_viaje.py."*

### Prompt 8: Encapsulamiento con Atributos Privados y Getters
> *"Modifica servicio_viaje.py: hacé privados los atributos __codigo, __precio_base y __reservado. Agrega los métodos públicos obtener_codigo(), obtener_precio_base() y esta_reservado(). Comenta cada línea."*

### Prompt 9: Refactorización a Decoradores `@property`
> *"Reemplaza los métodos obtener_codigo(), obtener_precio_base() y esta_reservado() por propiedades usando @property llamadas codigo, precio_base y reservado. Comenta qué hace @property."*

### Prompt 10: Prueba de Instancias Independientes
> *"Modifica main.py: crea dos servicios, s1 (código 'VUE123') y s2 (código 'HOT456'). Llama a reservar() solo en s1 y muestra el estado reservado de ambos demostrando su independencia."*

### Prompt 11: Método Base de Cálculo (`costo_total`)
> *"Agrega en servicio_viaje.py el método costo_total() que retorne el valor de precio_base. Comenta cada línea."*

### Prompt 12: Herencia (Subclases `Vuelo`, `Hotel`, `Excursion`)
> *"Crea tres archivos nuevos: vuelo.py, hotel.py y excursion.py. Hace que las clases Vuelo, Hotel y Excursion hereden de ServicioViaje. Déjalas vacías con pass por ahora e impórtalas en main.py."*

### Prompt 13: Constructor Propio en Subclase (`Hotel`)
> *"En hotel.py, agrégale a Hotel un atributo privado __noches. Escribe su constructor recibiendo codigo, precio_base y noches, llamando a super().__init__(codigo, precio_base). Agrega la propiedad @property noches."*

### Prompt 14: Polimorfismo (Sobrescritura de `costo_total`)
> *"Sobrescribe costo_total() en vuelo.py, hotel.py y excursion.py: Vuelo retorna precio_base + 25000 (tasa de embarque), Hotel retorna precio_base * noches, y Excursion retorna precio_base + 10000 (guía). Comenta cada línea."*

### Prompt 15: Validación de Datos con `@codigo.setter`
> *"En servicio_viaje.py, agrega el setter @codigo.setter validando que tenga al menos 6 caracteres y no contenga espacios; si no cumple, lanza un ValueError. En el constructor asigna self.codigo = codigo."*

### Prompt 16: Validaciones de Estado en `reservar()` y `cancelar()`
> *"Agrega validaciones en reservar() (lanzar ValueError si ya está reservado) y en cancelar() (lanzar ValueError si no estaba reservado). En main.py prueba un doble llamado a reservar() para verificar que el programa se detenga por la validación."*
