FROM python:3.12.0-alpine

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia solo el archivo de requerimientos primero para aprovechar la cache de Docker
COPY requirements.txt /app

# Instala pip y los requerimientos
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia el resto de tu código de aplicación
COPY . /app

# Instrucción para ejecutar tu aplicación FastAPI al iniciar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
