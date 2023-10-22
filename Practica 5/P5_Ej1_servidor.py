import http.server
import socketserver
import json
#import random

# Datos ficticios de geonames para ciudades
ciudades = {
    "Munich": {"latitud": -34.61, "longitud": -58.38},
    "Tokio": {"latitud": -22.91, "longitud": -43.20},
    "Santiago": {"latitud": -33.45, "longitud": -70.65},
    "Bogota": {"latitud": 4.61, "longitud": -74.08},
    "Toronto": {"latitud": 19.43, "longitud": -99.13},
}

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/geonames/'):
            ciudad = self.path[10:]
            if ciudad in ciudades:
                data = {"ciudad": ciudad, "latitud": ciudades[ciudad]["latitud"], "longitud": ciudades[ciudad]["longitud"]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("Ciudad no encontrada.".encode())  # Codificar la cadena a bytes
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9091), MyHandler) as httpd:
    print("Servidor de geonames en el puerto 9091")
    httpd.serve_forever()
