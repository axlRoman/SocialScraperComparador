import json

def texto_a_json(texto):
    datos = {}
    lineas = texto.split('\n')
    seccion_actual = None

    for linea in lineas:
        if ':' in linea:
            clave, valor = linea.split(':')
            clave = clave.strip()
            valor = valor.strip()
            datos[clave] = valor
            seccion_actual = clave
        elif seccion_actual is not None:
            datos[seccion_actual] = datos.get(seccion_actual, [])
            if isinstance(datos[seccion_actual], list):
                datos[seccion_actual].append(linea.strip())  # Usar append para agregar a la lista

    return datos

nombre_archivo_entrada = "datos.txt"
nombre_archivo_salida = "datos.json"  # Nombre del archivo JSON de salida

with open(nombre_archivo_entrada, "r", encoding="utf-8") as archivo_entrada:
    texto = archivo_entrada.read()

json_resultado = texto_a_json(texto)

with open(nombre_archivo_salida, "w", encoding="utf-8") as archivo_salida:
    # Utiliza json.dump() para escribir el JSON en un archivo
    json.dump(json_resultado, archivo_salida, indent=4, ensure_ascii=False)

print(f"Los datos han sido guardados en {nombre_archivo_salida}")
