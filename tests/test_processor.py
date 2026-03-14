# tests/test_processor.py

from processor import (
    calcular_promedio_avance,
    edad_maxima,
    edad_minima,
    conteo_por_linea,
    filtrar_por_avance
)


def test_calcular_promedio_avance_lista_vacia():
    estudiantes = []
    assert calcular_promedio_avance(estudiantes) == 0


def test_calcular_promedio_avance_valores_normales():
    estudiantes = [
        {"nombre": "Ana", "linea_investigacion": "Agroindustria", "edad": 29, "avance_tesis": 60},
        {"nombre": "Luis", "linea_investigacion": "Cadena de Valor", "edad": 31, "avance_tesis": 80}
    ]
    assert calcular_promedio_avance(estudiantes) == 70


def test_calcular_promedio_avance_valores_extremos():
    estudiantes = [
        {"nombre": "A", "linea_investigacion": "Agroindustria", "edad": 25, "avance_tesis": 0},
        {"nombre": "B", "linea_investigacion": "Cadena de Valor", "edad": 26, "avance_tesis": 100}
    ]
    assert calcular_promedio_avance(estudiantes) == 50


def test_edad_maxima():
    estudiantes = [
        {"nombre": "Ana", "linea_investigacion": "Agroindustria", "edad": 29, "avance_tesis": 60},
        {"nombre": "Luis", "linea_investigacion": "Cadena de Valor", "edad": 31, "avance_tesis": 80}
    ]
    assert edad_maxima(estudiantes) == 31


def test_edad_minima():
    estudiantes = [
        {"nombre": "Ana", "linea_investigacion": "Agroindustria", "edad": 29, "avance_tesis": 60},
        {"nombre": "Luis", "linea_investigacion": "Cadena de Valor", "edad": 31, "avance_tesis": 80}
    ]
    assert edad_minima(estudiantes) == 29


def test_conteo_por_linea():
    estudiantes = [
        {"nombre": "Ana", "linea_investigacion": "Agroindustria", "edad": 29, "avance_tesis": 60},
        {"nombre": "Luis", "linea_investigacion": "Agroindustria", "edad": 31, "avance_tesis": 80},
        {"nombre": "Carla", "linea_investigacion": "Biodiversidad", "edad": 28, "avance_tesis": 90}
    ]
    resultado = conteo_por_linea(estudiantes)
    assert resultado["Agroindustria"] == 2
    assert resultado["Biodiversidad"] == 1


def test_filtrar_por_avance():
    estudiantes = [
        {"nombre": "Ana", "linea_investigacion": "Agroindustria", "edad": 29, "avance_tesis": 60},
        {"nombre": "Luis", "linea_investigacion": "Cadena de Valor", "edad": 31, "avance_tesis": 80}
    ]
    resultado = filtrar_por_avance(estudiantes, 70)
    assert len(resultado) == 1
    assert resultado[0]["nombre"] == "Luis"