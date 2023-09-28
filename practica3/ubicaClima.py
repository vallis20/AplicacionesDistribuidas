import requests

def obtener_informacion_ubicacion(geonames_username, lugar):
    url = f"http://api.geonames.org/searchJSON?name={lugar}&maxRows=1&username={geonames_username}"


    try:
        response = requests.get(url)
        data = response.json()
        if "geonames" in data and data["geonames"]:
            ubicacion = data["geonames"][0]
            entrada = ubicacion['name']
            pais=ubicacion['countryName']
            return entrada, pais
        else:
            print("Ubicación no encontrada.")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
def obtener_datos_meteorologicos(ciudad,pais):
    url2 = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid=436bf84105f17c780c72730c5bd10d43"

    try:
        response = requests.get(url2)
        data = response.json()
        if "main" in data and "weather" in data:
            temperatura = data["main"]["temp"] - 273.15  # Convertir de Kelvin a Celsius
            condiciones_climaticas = data["weather"][0]["description"]
            print(f"Temperatura en {ciudad},{pais} : {temperatura:.2f}°C")
            print(f"Condiciones Climáticas en {ciudad},{pais}: {condiciones_climaticas}")
        else:
            print("Datos meteorológicos no disponibles.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Coloca tu usuario de geonames
    geonames_username = "vallis"
    lugar = "New York"  # Cambia esto a la ubicación que desees consultar
    nombre_ciudad,nombre_pais = obtener_informacion_ubicacion(geonames_username, lugar)
    if nombre_ciudad !=None:
        obtener_datos_meteorologicos(nombre_ciudad, nombre_pais)
