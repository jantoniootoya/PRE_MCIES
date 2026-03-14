# main.py

from data_loader import cargar_datos_csv
from processor import (
    filtrar_por_avance,
    filtrar_por_linea,
    filtrar_por_edad_minima,
    ordenar_por_nombre,
    ordenar_por_avance,
    ordenar_por_edad,
    generar_estadisticas
)
from exporter import exportar_a_json
from utils import LINEAS_VALIDAS


def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE TESIS - MAESTRÍA AGRONEGOCIOS UNALM ---")
    print("1 - Cargar datos desde CSV")
    print("2 - Filtrar datos")
    print("3 - Ordenar datos")
    print("4 - Mostrar estadísticas")
    print("5 - Exportar resultados a JSON")
    print("6 - Mostrar estudiantes cargados")
    print("7 - Salir")


def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes cargados.")
        return

    for i, est in enumerate(estudiantes, start=1):
        print(
            f"{i}. {est['nombre']} | "
            f"Línea: {est['linea_investigacion']} | "
            f"Edad: {est['edad']} | "
            f"Avance tesis: {est['avance_tesis']}%"
        )


def menu_filtros(estudiantes):
    if not estudiantes:
        print("Primero debes cargar datos.")
        return estudiantes

    print("\n--- FILTROS ---")
    print("1 - Filtrar por avance de tesis mayor a X")
    print("2 - Filtrar por línea de investigación")
    print("3 - Filtrar por edad mínima")

    opcion = input("Elige una opción: ").strip()

    try:
        if opcion == "1":
            minimo = float(input("Ingrese avance mínimo: "))
            filtrados = filtrar_por_avance(estudiantes, minimo)
            mostrar_estudiantes(filtrados)
            return filtrados

        elif opcion == "2":
            print("Líneas válidas:")
            for linea in LINEAS_VALIDAS:
                print("-", linea)
            linea = input("Ingrese línea de investigación: ").strip()
            filtrados = filtrar_por_linea(estudiantes, linea)
            mostrar_estudiantes(filtrados)
            return filtrados

        elif opcion == "3":
            edad = int(input("Ingrese edad mínima: "))
            filtrados = filtrar_por_edad_minima(estudiantes, edad)
            mostrar_estudiantes(filtrados)
            return filtrados

        else:
            print("Opción no válida.")
            return estudiantes

    except ValueError:
        print("Entrada inválida.")
        return estudiantes


def menu_orden(estudiantes):
    if not estudiantes:
        print("Primero debes cargar datos.")
        return estudiantes

    print("\n--- ORDENAR ---")
    print("1 - Ordenar por nombre")
    print("2 - Ordenar por avance de tesis")
    print("3 - Ordenar por edad")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        ordenados = ordenar_por_nombre(estudiantes)
    elif opcion == "2":
        ordenados = ordenar_por_avance(estudiantes)
    elif opcion == "3":
        ordenados = ordenar_por_edad(estudiantes)
    else:
        print("Opción no válida.")
        return estudiantes

    mostrar_estudiantes(ordenados)
    return ordenados


def main():
    estudiantes = []
    datos_actuales = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ruta = input("Ingrese la ruta del archivo CSV: ").strip()
            estudiantes = cargar_datos_csv(ruta)
            datos_actuales = estudiantes.copy()
            print(f"Se cargaron {len(estudiantes)} registros válidos.")

        elif opcion == "2":
            datos_actuales = menu_filtros(estudiantes)

        elif opcion == "3":
            datos_actuales = menu_orden(datos_actuales if datos_actuales else estudiantes)

        elif opcion == "4":
            base = datos_actuales if datos_actuales else estudiantes
            estadisticas = generar_estadisticas(base)
            print("\n--- ESTADÍSTICAS ---")
            for clave, valor in estadisticas.items():
                print(f"{clave}: {valor}")

        elif opcion == "5":
            base = datos_actuales if datos_actuales else estudiantes
            estadisticas = generar_estadisticas(base)
            ruta_salida = input("Ingrese la ruta de salida JSON: ").strip()
            exportar_a_json(estadisticas, ruta_salida)

        elif opcion == "6":
            base = datos_actuales if datos_actuales else estudiantes
            mostrar_estudiantes(base)

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()