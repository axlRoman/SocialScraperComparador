import json
import difflib

# Cargar los datos de los archivos JSON
def cargar_json(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

# Comparar dos estructuras JSON y calcular la similitud
def comparar_json(json1, json2):
    # Convierte las estructuras JSON en cadenas JSON
    str_json1 = json.dumps(json1, sort_keys=True, indent=4, ensure_ascii=False)
    str_json2 = json.dumps(json2, sort_keys=True, indent=4, ensure_ascii=False)

    # Calcula la similitud entre las dos cadenas JSON
    similarity_ratio = difflib.SequenceMatcher(None, str_json1, str_json2).ratio()
    
    return similarity_ratio

# Nombres de los archivos JSON a comparar
nombre_archivo_original = "datos_original.json"
nombre_archivo_convertido = "datos.json"

# Cargar los datos de los archivos JSON
datos_original = cargar_json(nombre_archivo_original)
datos_convertidos = cargar_json(nombre_archivo_convertido)

# Comparar las estructuras JSON y obtener la similitud
similitud = comparar_json(datos_original, datos_convertidos)

# Establecer un umbral de similitud para la evaluación
umbral_similitud = 0.9  # Puedes ajustar este valor según tus necesidades

# Realizar una evaluación basada en la similitud
if similitud >= umbral_similitud:
    evaluacion = "Muy similar"
elif similitud >= umbral_similitud/2 + .15:
    evaluacion = "Aceptable"
else:
    evaluacion = "No tan similar"

print(f"La similitud entre los datos es {similitud:.2f}")
print(f"Evaluación: {evaluacion}")
