import http.server
import socketserver
import json
import random

poblacion = {
    "Argentina": "44,938,712",
    "Brasil": "210,147,000",
    "Chile": "19,818,629",
    "Colombia": "50,374,000",
    "Mexico": "124,738,000",
    "Canada": "38,005,238",
}

capital = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile":"Santiago",
    "Colombia": "Bogotá",
    "Mexico":"Ciudad de México",
    "Canadá":"Ottawa"
}

ListasReproducion ={
    "Enanitos Verdes",
    "Today's Hits",
    "Fiesta",
    "Cumbia pa' la fiesta",
    "Luis Miguel",
    "Voces de México",
    "La oficial",
    "Rock de los 80's",
    "¡Dale play!",
    "Waking up",
    "Halloween",
    "Puro pop",
    "Hits virales",
    "Salsa"
    }

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/temperature/'):
            pais = self.path[13:]
            if pais in poblacion:
                data = {"population": poblacion[pais]}
               
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())  # Codificar la cadena a bytes
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090")
    httpd.serve_forever()
