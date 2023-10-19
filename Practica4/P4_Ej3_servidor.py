import http.server
import socketserver
import requests

# Tu API Key de Geonames
GEONAMES_API_KEY = "migfel"

# Tu API Key de OpenWeatherMap
OPENWEATHERMAP_API_KEY = "513e279c8528809604d582135090e41f"

# Función para obtener información de ubicación desde Geonames
def obtener_informacion_geonames(ciudad):
    geonames_url = f"http://api.geonames.org/searchJSON?q={ciudad}&maxRows=1&username={GEONAMES_API_KEY}"
    response = requests.get(geonames_url)
    data = response.json()
    return data

# Función para obtener datos meteorológicos desde OpenWeatherMap
def obtener_datos_meteorologicos(latitud, longitud):
    openweathermap_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={OPENWEATHERMAP_API_KEY}"
    response = requests.get(openweathermap_url)
    data = response.json()
    return data

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/weather/'):
            ciudad = self.path[9:]
            geonames_data = obtener_informacion_geonames(ciudad)
            
            if "geonames" in geonames_data and geonames_data["geonames"]:
                location = geonames_data["geonames"][0]
                latitud = location["lat"]
                longitud = location["lng"]
                openweathermap_data = obtener_datos_meteorologicos(latitud, longitud)

                if "main" in openweathermap_data and "weather" in openweathermap_data:
                    temperatura = openweathermap_data["main"]["temp"] - 273.15  # Convertir de Kelvin a Celsius
                    condiciones_climaticas = openweathermap_data["weather"][0]["description"]
                    resultado = f"Temperatura: {temperatura:.2f}°C<br>Condiciones Climáticas: {condiciones_climaticas}"
                else:
                    resultado = "Datos meteorológicos no disponibles."

            else:
                resultado = "Ubicación no encontrada."
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(resultado.encode())
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090 para Geonames y OpenWeatherMap")
    httpd.serve_forever()
