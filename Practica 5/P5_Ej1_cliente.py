import requests

# URL del servidor de geonames (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9091'

def obtener_datos_geonames(ciudad):
    url = f'{url_base}/geonames/{ciudad}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'Datos de {ciudad}: Latitud {data["latitud"]}, Longitud {data["longitud"]}'
    elif response.status_code == 404:
        return f'Ciudad no encontrada: {ciudad}'
    else:
        return f'Error en la solicitud: Codigo {response.status_code}'

# Ejemplos de uso
ciudades = ["Munich", "Tokio", "Santiago", "Bogota", "Toronto"]
for ciudad in ciudades:
    resultado = obtener_datos_geonames(ciudad)
    print(resultado)
