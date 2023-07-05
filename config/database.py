import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#nombre de la db
#los ../ indican que cree la db una carpeta antes (en la raiz del proyecto)
sqlite_file_name = "../database.sqlite"

#de esta forma leemos el directorio actual (database.py)
base_dir = os.path.dirname(os.path.realpath(__file__))

#esta es la url de mi db
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

#motor de la db
#echo me muestra por consola lo que se este realizando al momento de crear la db
engine = create_engine(database_url, echo=True)

#sesion para conectarme a la db
Session = sessionmaker(bind=engine)

Base = declarative_base()
