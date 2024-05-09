# Utiliza una imagen base de Python en su versión Alpine para menor tamaño de imagen
FROM python:3.12.0-alpine

# Establece el directorio de trabajo en /app dentro del contenedor
WORKDIR /app

# Copia solo el archivo de requerimientos primero para aprovechar la cache de Docker
COPY requirements.txt /app

# Instala pip y los requerimientos necesarios para tu aplicación
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia los certificados SSL desde tu directorio local al directorio /etc/ssl/certs dentro del contenedor
COPY certificates/server-ca.pem /etc/ssl/certs/
COPY certificates/client-cert.pem /etc/ssl/certs/
COPY certificates/client-key.pem /etc/ssl/certs/

# Copia el resto de tu código de aplicación
COPY . /app

# Instrucción para ejecutar tu aplicación FastAPI al iniciar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
