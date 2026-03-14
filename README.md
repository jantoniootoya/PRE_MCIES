# DataManager - Gestión de estudiantes de Maestría en Agronegocios UNALM

Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en Python para gestionar información de los estudiantes de la Maestría en Agronegocios de la Universidad Nacional Agraria La Molina (UNALM).

El sistema permite:

- Cargar datos desde archivos CSV
- Validar y limpiar registros
- Filtrar estudiantes
- Ordenar datos
- Generar estadísticas básicas
- Exportar resultados en formato JSON
- Ejecutar pruebas unitarias con pytest

El objetivo del proyecto es aplicar conceptos fundamentales de programación en Python como manejo de archivos, estructuras de datos, modularización del código, manejo de errores y testing automatizado.

---

# Estructura del proyecto

datamanager/
│
├── main.py
├── data_loader.py
├── processor.py
├── exporter.py
├── utils.py
├── README.md
│
├── data/
│   └── estudiantes_maestria.csv
│
├── output/
│   └── resultados.json
│
└── tests/
    └── test_processor.py


Descripción de los módulos principales:

| Archivo | Descripción |
|------|------|
| main.py | Programa principal y menú CLI |
| data_loader.py | Lectura y validación de datos CSV |
| processor.py | Funciones de filtrado, ordenamiento y estadísticas |
| exporter.py | Exportación de resultados en JSON |
| utils.py | Funciones de validación de datos |
| tests | Pruebas unitarias con pytest |

---

# Estructura de los datos

Cada estudiante tiene la siguiente información:

| Campo | Tipo | Descripción |
|-----|-----|-----|
| nombre | string | Nombre y apellido del estudiante |
| linea_investigacion | string | Línea de investigación |
| edad | int | Edad del estudiante |
| avance_tesis | float | Porcentaje de avance de tesis (0–100) |

Ejemplo de registro:

nombre,linea_investigacion,edad,avance_tesis
Ana Torres,Agroindustria,29,65.5

---

# Líneas de investigación consideradas

El sistema reconoce las siguientes líneas:

- Agro-exportacion
- Cadena de Valor
- Agricultura familiar
- Fomento agrario
- Agroindustria
- Nuevos productos
- Biodiversidad
- Características de consumidor

---

# Requisitos

Python 3.9 o superior

Instalar pytest para ejecutar los tests:

pip install pytest

---

# Ejecución del programa

Para ejecutar el programa desde la terminal:

python main.py

Aparecerá el siguiente menú:

--- SISTEMA DE GESTIÓN DE TESIS - MAESTRÍA AGRONEGOCIOS UNALM ---

1 - Cargar datos desde CSV
2 - Filtrar datos
3 - Ordenar datos
4 - Mostrar estadísticas
5 - Exportar resultados a JSON
6 - Mostrar estudiantes cargados
7 - Salir

---

# Ejemplos de uso

## 1. Cargar datos desde CSV

Seleccionar opción:

1

Luego ingresar la ruta del archivo:

Ejemplo: data/estudiantes_maestria.csv

Salida esperada:

Se cargaron 33 registros válidos.

---

## 2. Mostrar estudiantes cargados

Seleccionar opción:

6

Ejemplo de salida:

1. Ana Torres | Línea: Agroindustria | Edad: 29 | Avance tesis: 65.5%
2. Luis Ramírez | Línea: Cadena de Valor | Edad: 31 | Avance tesis: 80%
3. Carla Mendoza | Línea: Biodiversidad | Edad: 28 | Avance tesis: 92.3%

---

## 3. Filtrar por avance de tesis

Seleccionar opción:

2

Luego:

1 - Filtrar por avance de tesis mayor a X

Ejemplo:

Ingrese avance mínimo: 90

Resultado:

Carla Mendoza | Biodiversidad | 92.3%
Pedro Salazar | Agro-exportacion | 95%

---

## 4. Ordenar estudiantes por avance de tesis

Seleccionar opción:

3

Luego:

2 - Ordenar por avance de tesis

Resultado esperado (orden descendente):

1. Pedro Salazar | 95%
2. Carla Mendoza | 92.3%
3. Luis Ramírez | 80%

---

## 5. Mostrar estadísticas

Seleccionar opción:

4

Ejemplo de salida:

promedio_avance_tesis: 61.4
edad_maxima: 35
edad_minima: 26
total_estudiantes: 33
conteo_por_linea: {
"Agroindustria": 5,
"Cadena de Valor": 4,
"Biodiversidad": 3
}

---

## 6. Exportar resultados a JSON

Seleccionar opción:

5

Ingresar ruta de salida:

1

Mensaje:

Resultados exportados correctamente a: output/resultados.json

Ejemplo del archivo generado:

{
"promedio_avance_tesis": 61.4,
"edad_maxima": 35,
"edad_minima": 26,
"total_estudiantes": 33,
"conteo_por_linea": {
"Agroindustria": 5,
"Cadena de Valor": 4,
"Biodiversidad": 3
}
}

---

# Ejecutar pruebas unitarias

Desde la raíz del proyecto ejecutar:

pytest

Resultado esperado:

================ test session starts ================
6 passed in 0.03s

Las pruebas verifican:

- cálculo del promedio de avance
- edad máxima y mínima
- conteo por línea de investigación
- filtrado por avance

---

# Autor
Mg. Sc. (c) José Otoya-Barrenechea
https://orcid.org/0009-0007-0702-6958
Proyecto académico desarrollado para práctica de programación en Python aplicando manejo de datos, modularización y testing.
"""

path = "/PRE_MCIES/README.md"