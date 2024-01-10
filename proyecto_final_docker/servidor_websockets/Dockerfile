# Utiliza una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias
# Instalar dependencias del sistema
RUN apt-get update \
    && apt-get install -y unixodbc-dev


# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5555
EXPOSE 5555

# Comando para ejecutar el servidor de WebSockets
CMD ["python", "servidor_websockets.py"]
