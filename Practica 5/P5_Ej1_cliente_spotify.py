import requests

# URL del servidor de la lista de reproducción (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9092'

def obtener_lista_de_reproduccion():
    url = f'{url_base}/playlist'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        canciones = data["canciones"]
        return "Lista de Reproducción de Spotify en Mexico:\n" + "\n".join([f'{c["nombre"]} - {c["artista"]} ({c["duracion"]})' for c in canciones])
    elif response.status_code == 404:
        return "Ruta no encontrada."
    else:
        return f'Error en la solicitud: Código {response.status_code}'

# Ejemplo de uso
resultado = obtener_lista_de_reproduccion()
print(resultado)
