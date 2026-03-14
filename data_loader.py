# data_loader.py

import csv
from utils import validar_estudiante


def cargar_datos_csv(ruta_archivo):
    estudiantes = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    estudiante = {
                        "nombre": fila["nombre"].strip(),
                        "linea_investigacion": fila["linea_investigacion"].strip(),
                        "edad": int(fila["edad"]),
                        "avance_tesis": float(fila["avance_tesis"])
                    }

                    if validar_estudiante(estudiante):
                        estudiantes.append(estudiante)
                    else:
                        print(f"Registro inválido omitido: {fila}")

                except ValueError:
                    print(f"Error de conversión en fila: {fila}")
                except KeyError:
                    print("El archivo CSV no tiene las columnas esperadas.")
                    return []

    except FileNotFoundError:
        print("Error: no se encontró el archivo.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return []

    return estudiantes