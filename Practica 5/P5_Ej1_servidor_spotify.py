import http.server
import socketserver
import json
import random

# Datos ficticios de canciones para una lista de reproducción de Spotify
canciones = [
    {"nombre": "Que onda", "artista": "Calle 24 x Chino Pacas x Fuerza Regida", "duracion": "3:11"},
    {"nombre": "LADY GAGA", "artista": "Peso Pluma, Gabito Ballesteros, Junior H", "duracion": "3:32"},
    {"nombre": "ELOVRGA", "artista": "Añex Favela, Grupo Marca Registrada, Joaquin Medina", "duracion": "3:14"},
    {"nombre": "PERRO NEGRO", "artista": "Bad Bunny, Feid", "duracion": "2:42"},
    {"nombre": "Y LLORO", "artista": "Junior H", "duracion": "2:59"},
]

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/playlist':
            data = {"canciones": canciones}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Ruta no encontrada.".encode())

# Configuración del servidor
with socketserver.TCPServer(("", 9092), MyHandler) as httpd:
    print("Servidor de lista de reproducción en el puerto 9092")
    httpd.serve_forever()
