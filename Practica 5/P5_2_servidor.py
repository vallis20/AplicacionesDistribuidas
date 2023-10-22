import http.server
import socketserver
import json
import random

# Datos ficticios de clima 
paises = {
    "Argentina": {"temperatura": random.uniform(25, 30), "clima":"Soleado"},
    "Brasil": {"temperatura": random.uniform(25, 30), "clima":"Parcialmente_nublado"},
    "Chile": {"temperatura": random.uniform(9, 15), "clima":"Nublado"},
    "Colombia": {"temperatura": random.uniform(6, 17), "clima":"Mayormente_nublado"},
    "Mexico": {"temperatura": random.uniform(14, 27), "clima":"Parcialmente_nublado"},
    "Canada": {"temperatura": random.uniform(3, 8), "clima":"Despejado_con_intervalos_nublosos"},
    "USA": {"temperatura": random.uniform(7, 16), "clima":"Mayormente_nublado"},
    "Alemania": {"temperatura": random.uniform(8, 16), "clima":"Nublado"},
}

# Datos de listas de reproducción de Spotify
listasReproducion ={
    "Argentina": {"listas": ["Argentina_Mix", "Éxitos_Argentina", "TOP_ARGENTINA"]},
    "Brasil": {"listas": ["Brasil_Mix", "Éxitos_Brasil", "TOP_Brasil"]},
    "Chile": {"listas": ["Chile_Mix", "Éxitos_Chile", "TOP_Chile"]},
    "Colombia": {"listas": ["Colombia_Mix", "Éxitos_Colombia", "TOP_Colombia"]},
    "Mexico": {"listas": ["México_Mix", "Éxitos_México", "TOP_México"]},
    "Canada": {"listas": ["Canada_Mix", "Éxitos_Canada", "TOP_Canada"]},
    "USA": {"listas": ["USA_Mix", "Éxitos_USA", "TOP_USA"]},
    "Alemania": {"listas": ["Alemania_Mix", "Éxitos_Alemania", "TOP_Alemania"]},
}

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/temperature/'):
            pais = self.path[13:]
            if pais in paises:
                data = {"pais": pais, "temperatura": paises[pais]["temperatura"], "clima": paises[pais]["clima"]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())

        elif self.path.startswith('/playlist/'):
            pais = self.path[10:]
            if pais in listasReproducion:
                data = {"pais": pais, "listas": listasReproducion[pais]["listas"]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())

        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor en el puerto 9090")
    httpd.serve_forever()

