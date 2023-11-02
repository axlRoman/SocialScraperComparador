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
            # Asegurarse de que la sección actual sea una lista
            datos[seccion_actual] = datos.get(seccion_actual, [])
            if isinstance(datos[seccion_actual], list):
                datos[seccion_actual].append(linea.strip())  # Usar append para agregar a la lista

    return datos

nombre_archivo = "datos.txt"

with open(nombre_archivo, "r", encoding="utf-8") as archivo:  # Lee el archivo con codificación UTF-8
    texto = archivo.read()

json_resultado = texto_a_json(texto)

# Configura ensure_ascii en False al utilizar json.dumps
# Esto permitirá que los caracteres no ASCII se muestren correctamente en el JSON.
json_output = json.dumps(json_resultado, indent=4, ensure_ascii=False)

print(json_output)

