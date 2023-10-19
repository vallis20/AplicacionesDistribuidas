import http.server
import socketserver
import requests

# Tu nombre de usuario de Geonames
GEONAMES_USERNAME = "migfel"

# Función para obtener datos de Geonames
def obtener_datos_geonames(ciudad):
    base_url = "http://api.geonames.org/searchJSON"
    params = {
        "q": ciudad,
        "maxRows": 1,
        "username": GEONAMES_USERNAME,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if "geonames" in data and data["geonames"]:
            lugar = data["geonames"][0]
            poblacion = lugar.get("population")
            pais = lugar.get("countryName")
            return f"Población: {población}<br>País: {pais}"
        else:
            return "Datos de Geonames no disponibles."
    except Exception as e:
        return f"Error: {str(e)}"

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/geonames/'):
            ciudad = self.path[10:]
            resultado = obtener_datos_geonames(ciudad)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(resultado.encode())
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090 para Geonames")
    httpd.serve_forever()
