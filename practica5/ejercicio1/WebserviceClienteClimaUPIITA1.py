import requests

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9090'

def obtener_datos_pais(pais):
    #url = f'{url_base}/geonames/{pais}'
    url = f'{url_base}/geonames/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'Poblacion en {pais}: {data["geonames"]}'
        #return f'Poblacion en {pais}: {data["Poblacion"], "Capital": data["Capital"]}'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

# Ejemplos de uso
paises = ["Argentina", "Brasil", "Chile", "Colombia", "Mexico"]
for pais in paises:
    resultado = obtener_datos_pais(pais)
    print(resultado)
