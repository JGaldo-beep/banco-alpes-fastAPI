import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Variables para configurar la conexión a PostgreSQL usando variables de entorno
username = os.getenv('DB_USERNAME', 'myuser')
password = os.getenv('DB_PASSWORD', 'password-fastapi')
host = os.getenv('DB_HOST', '35.226.62.13')
port = os.getenv('DB_PORT', '5432')  # El puerto estándar de PostgreSQL es 5432
database = os.getenv('DB_DATABASE', 'fastapi_database')

database_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

connect_args = {
    'sslmode': 'verify-ca',
    'sslrootcert': '/etc/ssl/certs/server-ca.pem',
    'sslcert': '/etc/ssl/certs/client-cert.pem',
    'sslkey': '/etc/ssl/certs/client-key.pem'
}

# Crear el motor con un pool de conexiones y argumentos de conexión SSL
engine = create_engine(database_url, echo=True, pool_size=30, max_overflow=70, pool_timeout=30, pool_recycle=1800, connect_args=connect_args)

Session = sessionmaker(bind=engine)
Base = declarative_base()
