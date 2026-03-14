# processor.py

def filtrar_por_avance(estudiantes, minimo):
    resultado = []
    for est in estudiantes:
        if est["avance_tesis"] > minimo:
            resultado.append(est)
    return resultado


def filtrar_por_linea(estudiantes, linea):
    resultado = []
    for est in estudiantes:
        if est["linea_investigacion"].lower() == linea.lower():
            resultado.append(est)
    return resultado


def filtrar_por_edad_minima(estudiantes, edad_minima):
    resultado = []
    for est in estudiantes:
        if est["edad"] >= edad_minima:
            resultado.append(est)
    return resultado


def ordenar_por_nombre(estudiantes):
    return sorted(estudiantes, key=lambda x: x["nombre"].lower())


def ordenar_por_avance(estudiantes):
    return sorted(estudiantes, key=lambda x: x["avance_tesis"], reverse=True)


def ordenar_por_edad(estudiantes):
    return sorted(estudiantes, key=lambda x: x["edad"])


def calcular_promedio_avance(estudiantes):
    if len(estudiantes) == 0:
        return 0
    suma = 0
    for est in estudiantes:
        suma += est["avance_tesis"]
    return round(suma / len(estudiantes), 2)


def edad_maxima(estudiantes):
    if len(estudiantes) == 0:
        return None
    return max(est["edad"] for est in estudiantes)


def edad_minima(estudiantes):
    if len(estudiantes) == 0:
        return None
    return min(est["edad"] for est in estudiantes)


def conteo_por_linea(estudiantes):
    conteo = {}
    for est in estudiantes:
        linea = est["linea_investigacion"]
        if linea in conteo:
            conteo[linea] += 1
        else:
            conteo[linea] = 1
    return conteo


def generar_estadisticas(estudiantes):
    return {
        "promedio_avance_tesis": calcular_promedio_avance(estudiantes),
        "edad_maxima": edad_maxima(estudiantes),
        "edad_minima": edad_minima(estudiantes),
        "total_estudiantes": len(estudiantes),
        "conteo_por_linea": conteo_por_linea(estudiantes)
    }