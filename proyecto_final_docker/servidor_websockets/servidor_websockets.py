import asyncio
import websockets
import http.server
import socketserver
import os
from websockets.exceptions import ConnectionClosedOK
from connectionbd import BaseDatos
from informes import generate_general_report, generate_billing_report

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="./")

#DESCARGAR
async def websocket_handler(websocket, path):
    async for message in websocket:
        print(message)
        if message == 'subir_archivo':
                print("Recibida solicitud para subir archivo")
                websocket.max_size = 100 * 1024 * 1024  # 100MB

                # Recibe el nombre del archivo y su tamaño
                file_info = await websocket.recv()
                file_name, file_size = file_info.split(',')
                file_size = int(file_size)

                folder_name = "archivos_recibidos"
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)

                uploaded_file_name = os.path.join(folder_name, file_name.strip())  # Ruta completa del archivo
                with open(uploaded_file_name, 'ab') as file:
                    received_size = 0
                    while received_size < file_size:
                        chunk = await websocket.recv()  # Recibe chunks de 10MB
                        if not chunk:
                            break
                        file.write(chunk)
                        received_size += len(chunk)

                        # Calcula y envía el progreso cada 10MB
                        progress = (received_size / file_size) * 100
                        if received_size % (10 * 1024 * 1024) == 0:
                            await websocket.send(f"Progreso: {progress}%")

                    # Envía la URL del archivo al cliente al finalizar
                    file_path = os.path.abspath(uploaded_file_name)
                    file_url = f'http://localhost:8080/{uploaded_file_name}'
                    await websocket.send(file_url)
                    print(f"URL del archivo enviado al cliente: {file_url}")

        if message == 'descargar_archivo':
            print("Solicitud recibida para descargar archivo")
            file_name = "video.mp4"  
            file_path = os.path.join("archivos_recibidos", file_name)  

            if os.path.exists(file_path) and os.path.isfile(file_path):
                try:
                    file_url = f'http://localhost:8080/archivos_recibidos/{file_name}'
                    await websocket.send(file_url)
                    print(f"URL del archivo enviada al cliente: {file_url}")
                except Exception as e:
                    print(f"Error al enviar la URL del archivo: {str(e)}")
            else:
                await websocket.send("Archivo no encontrado")

        if message == 'generar_reporte_general':
            print("Recibida solicitud para generar el reporte.")
            try:
                bd = BaseDatos()  # Instanciamos la clase BaseDatos
                bd.connect()  # Conexión a la base de datos
                nombreA = "General_Statistics_Report.pdf"
                generate_general_report(bd, nombreA)
                bd.disconnect()
                print("Reporte generado con éxito.")
                
                # Enviar la ruta del archivo al cliente
                file_path = os.path.abspath(nombreA)
                await websocket.send(f'http://localhost:8080/{nombreA}')
                print(f"URL del reporte enviado al cliente: http://localhost:8080/{nombreA}")
            except Exception as e:
                print(f"Error al generar el reporte: {str(e)}")

        if message == 'generar_reporte_facturacion':
            print("Recibida solicitud para generar el reporte.")
            try:
                bd = BaseDatos()  # Instanciamos la clase BaseDatos
                bd.connect()  # Conexión a la base de datos
                generate_billing_report(bd)
                bd.disconnect()
                nombreA = "Billing_Statistics_Report.pdf"
                print("Reporte generado con éxito.")
                
                # Enviar la ruta del archivo al cliente
                file_path = os.path.abspath(nombreA)
                await websocket.send(f'http://localhost:8080/{nombreA}')
                print(f"URL del reporte enviado al cliente: http://localhost:8080/{nombreA}")
            except Exception as e:
                print(f"Error al generar el reporte: {str(e)}")

async def main():
    http_server = socketserver.TCPServer(('localhost', 8080), HTTPRequestHandler)
    http_server_thread = asyncio.get_event_loop().run_in_executor(None, http_server.serve_forever)

    start_server = websockets.serve(websocket_handler, "localhost", 5555)

    await asyncio.gather(
        start_server,
        http_server_thread,
    )

if __name__ == "__main__":
    print("Servidor esperando conexiones...")
    asyncio.run(main())