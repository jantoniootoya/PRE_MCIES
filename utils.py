LINEAS_VALIDAS = [
    "Agro-exportacion",
    "Cadena de Valor",
    "Agricultura familiar",
    "Fomento agrario",
    "Agroindustria",
    "Nuevos productos",
    "Biodiversidad",
    "Características de consumidor"
]


def validar_nombre(nombre):
    if not isinstance(nombre, str):
        return False
    if nombre.strip() == "":
        return False
    return True


def validar_linea_investigacion(linea):
    if not isinstance(linea, str):
        return False
    return linea.strip() in LINEAS_VALIDAS


def validar_edad(edad):
    try:
        edad = int(edad)
        return edad > 0
    except (ValueError, TypeError):
        return False


def validar_avance_tesis(avance):
    try:
        avance = float(avance)
        return 0 <= avance <= 100
    except (ValueError, TypeError):
        return False


def validar_estudiante(estudiante):
    """
    Valida si un diccionario de estudiante tiene campos correctos.
    """
    try:
        return (
            validar_nombre(estudiante.get("nombre")) and
            validar_linea_investigacion(estudiante.get("linea_investigacion")) and
            validar_edad(estudiante.get("edad")) and
            validar_avance_tesis(estudiante.get("avance_tesis"))
        )
    except Exception:
        return False