import http.server
import socketserver
import json
import random

# Datos ficticios de temperatura para países de América Latina
Poblacion = {
    "Argentina": random.uniform(5, 30),
    "Brasil": random.uniform(20, 40),
    "Chile": random.uniform(5, 25),
    "Colombia": random.uniform(20, 35),
    "Mexico": random.uniform(10, 30),
    "Canadá": random.uniform(10, 30)

}

Capital = {
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
    "Peso pluma",
    "Waking up",
    "Halloween",
    "Puro pop",
    "Hits virales",
    "Salsa"
    }
    
# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/geonames/'):
            pais = self.path[13:]
            #Servicios de geonmes
            print("*Geonames")
            if pais in Poblacion and pais in Capital:
                data1 = {"Poblacion  ": Poblacion[pais]}
                #data1 = {pais: {"Poblacion": Poblacion[pais], "Capital": Capital[pais]} for pais in Poblacion}
                print(data1)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data1).encode())  # Codificar la cadena a bytes

                

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
