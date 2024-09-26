import os

# Estructura de directorios y archivos base para un proyecto FastAPI
def estructura_base(nombre_proyecto, incluir_db=False, incluir_orm=False):
    estructura = {
        nombre_proyecto: {
            'app': {
                'api': {
                    '__init__.py': '',
                    'v1': {
                        '__init__.py': '',
                        'routes.py': '# Aquí se definen las rutas de la API v1\n\nfrom fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.get("/")\ndef read_root():\n    return {"message": "Hello from API v1!"}',
                    }
                },
                'core': {
                    '__init__.py': '',
                    'config.py': '# Configuración general\n\nclass Settings:\n    PROJECT_NAME: str = "FastAPI Project"\n    API_V1_STR: str = "/api/v1"\nsettings = Settings()',
                    'security.py': '# Autenticación y seguridad',
                },
                'models': {
                    '__init__.py': '',
                },
                'schemas': {
                    '__init__.py': '',
                },
                'repositories': {
                    '__init__.py': '',
                },
                'services': {
                    '__init__.py': '',
                },
                'main.py': '''# Punto de entrada de la aplicación FastAPI
from fastapi import FastAPI
from app.api.v1.routes import router as api_v1_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Incluir las rutas de la API v1
app.include_router(api_v1_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
''',
            },
            'requirements.txt': '# Dependencias\nfastapi\nuvicorn',
            'README.md': f'# {nombre_proyecto}\n\nDescripción del proyecto basado en FastAPI.',
        }
    }

    # Si se selecciona incluir configuración de base de datos
    if incluir_db:
        estructura[nombre_proyecto]['app']['database.py'] = '''# Configuración de la base de datos
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Cambiar por la URL de la base de datos deseada

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependiendo de tu ORM, ajusta el archivo.
'''
        estructura[nombre_proyecto]['requirements.txt'] += '\nsqlalchemy\nsqlite3'

    # Si se selecciona incluir un ORM (SQLAlchemy en este caso)
    if incluir_orm:
        estructura[nombre_proyecto]['app']['models']['__init__.py'] = '''# Modelos de la base de datos con SQLAlchemy
from sqlalchemy import Column, Integer, String
from app.database import Base

class ExampleModel(Base):
    __tablename__ = "example_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
'''
        estructura[nombre_proyecto]['requirements.txt'] += '\nfastapi[sqlalchemy]\n'

    return estructura

# Función para crear la estructura de directorios y archivos
def crear_estructura(base_path, estructura):
    for nombre, contenido in estructura.items():
        ruta = os.path.join(base_path, nombre)
        if isinstance(contenido, dict):
            # Si el contenido es un diccionario, es un directorio
            os.makedirs(ruta, exist_ok=True)
            crear_estructura(ruta, contenido)  # Recursión para subdirectorios
        else:
            # Si no es un diccionario, es un archivo
            with open(ruta, 'w') as archivo:
                archivo.write(contenido)

# Función para interactuar con el usuario
def solicitar_informacion():
    nombre_proyecto = input('Ingresa el nombre del proyecto: ')
    incluir_db = input('¿Quieres incluir la configuración de base de datos? (s/n): ').lower() == 's'
    incluir_orm = input('¿Quieres usar un ORM (SQLAlchemy)? (s/n): ').lower() == 's'
    return nombre_proyecto, incluir_db, incluir_orm

if __name__ == '__main__':
    # Solicitar información al usuario
    nombre_proyecto, incluir_db, incluir_orm = solicitar_informacion()

    # Directorio raíz
    base_dir = os.path.join(os.getcwd())

    # Crear la estructura de carpetas y archivos
    estructura = estructura_base(nombre_proyecto, incluir_db, incluir_orm)
    crear_estructura(base_dir, estructura)

    print(f'Estructura del proyecto {nombre_proyecto} creada en: {base_dir}')
