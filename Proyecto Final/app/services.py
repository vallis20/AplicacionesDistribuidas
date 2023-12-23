import os

current_status = "online"

def set_status(status):
    global current_status
    current_status = status

def get_status():
    return current_status

class FileService:
    @staticmethod
    def upload_file(file):
        try:
            # Verifica si el directorio de carga existe, si no, créalo
            upload_folder = 'uploads'
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            # Guarda el archivo en el directorio de carga
            file_path = os.path.join(upload_folder, file.filename)
            file.save(file_path)

            # Puedes realizar más procesamiento aquí, como almacenar información en la base de datos

            return file_path  # Devuelve la ruta del archivo guardado
        except Exception as e:
            # Maneja cualquier error que pueda ocurrir durante la carga del archivo
            print(f"Error al cargar el archivo: {e}")
            return None

    @staticmethod
    def download_file(file_id):
        try:
            # Supongamos que file_id es el nombre del archivo (puedes ajustar esto según tus necesidades)
            file_path = os.path.join('uploads', file_id)

            # Verifica si el archivo existe antes de intentar descargarlo
            if os.path.exists(file_path):
                return file_path  # Devuelve la ruta del archivo
            else:
                return None  # Archivo no encontrado
        except Exception as e:
            # Maneja cualquier error que pueda ocurrir durante la descarga del archivo
            print(f"Error al descargar el archivo: {e}")
            return None