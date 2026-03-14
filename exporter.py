# exporter.py

import json


def exportar_a_json(datos, ruta_salida):
    try:
        with open(ruta_salida, mode="w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"Resultados exportados correctamente a: {ruta_salida}")
    except Exception as e:
        print(f"Error al exportar JSON: {e}")