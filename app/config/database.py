import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base # manipulate tables in db

# Variables para configurar la conexión a PostgreSQL
username = 'myuser'
password = 'password-fastapi'
host = '35.226.62.13'
port = '5432'  # El puerto estándar de PostgreSQL es 5432
database = 'fastapi_database'

# base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(database_url, echo=True, pool_size=30, max_overflow=70, pool_timeout=30, pool_recycle=1800)

Session = sessionmaker(bind=engine)

Base = declarative_base()