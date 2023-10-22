import requests


# URL del servidor de geonames (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9090'

def obtener_clima(pais):
    url = f'{url_base}/temperature/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        #print(data)
        return f'Pais: {pais} -> temperatura: {data["temperatura"]:.2f}°C, clima: {data["clima"]}'
    elif response.status_code == 404:
        return "País no encontrado"
    else:
        return f'Error en la solicitud: Código {response.status_code}'


def obtener_playlist(pais):
    url = f'{url_base}/playlist/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        #print(data)
        return f'Pais: {pais} -> listas más populares: {data["listas"]}'
    elif response.status_code == 404:
        return "País no encontrado"
    else:
        return f'Error en la solicitud: Código {response.status_code}'


 #Ejemplos de uso
paises = ["Argentina", "Brasil", "Chile", "Canada"]
for pais in paises:
    resultado = obtener_clima(pais)
    print(resultado)

    resultado  = obtener_playlist(pais)
    print(resultado)
