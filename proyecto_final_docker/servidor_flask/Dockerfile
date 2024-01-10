# Utiliza una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instalar las dependencias del sistema
RUN apt-get update \
    && apt-get install -y unixodbc unixodbc-dev libodbc1 \
    && rm -rf /var/lib/apt/lists/*


# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias
#RUN apt-get update \
#    && apt-get install -y build-essential \
#                           libpq-dev \
#                           libjpeg-dev \
#                           zlib1g-dev \
#                           libfreetype6-dev

RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "servidor_flask.py"]
