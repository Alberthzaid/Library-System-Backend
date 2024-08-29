FROM python:3.11-slim

LABEL authors="Library-Backend"

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos a la imagen
COPY requirements.txt requirements.txt

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación a la imagen
COPY . .

# Define la variable de entorno para Flask
ENV FLASK_APP=app.py

# Expone el puerto en el que la app de Flask correrá
EXPOSE 5000

# Comando para correr la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]

