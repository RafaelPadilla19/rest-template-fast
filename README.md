# FastAPI Project Template Generator

Este script en Python está diseñado para automatizar la creación de una plantilla de proyecto **FastAPI** bien estructurada. Permite a los desarrolladores configurar rápidamente un proyecto FastAPI con opciones para la configuración de la base de datos y la integración de un ORM (SQLAlchemy).

## Características

- **Configuración de FastAPI**: Genera una base inicial para proyectos FastAPI, incluyendo archivos necesarios y una estructura de directorios que facilita el desarrollo.
  
- **Integración de Base de Datos** (Opcional): Permite al usuario decidir si desea incluir una configuración de base de datos al iniciar el proyecto. Puedes elegir entre varias opciones de bases de datos, como SQLite o PostgreSQL.

- **Modelos ORM** (Opcional): Si decides incluir la configuración de la base de datos, el script generará modelos ORM utilizando SQLAlchemy para facilitar la interacción con la base de datos.

- **Personalizable**: El script interactúa con el usuario, solicitando información como el nombre del proyecto y otras configuraciones relevantes, lo que permite personalizar la estructura según las necesidades del desarrollador.

## Estructura de Carpetas y Archivos

El script genera una estructura de directorios y archivos que sigue las mejores prácticas para proyectos FastAPI:

- **`app/`**: Contiene toda la lógica de la aplicación.
  - **`api/`**: Define las rutas y controladores de la API.
    - **`__init__.py`**: Indica que este directorio debe ser tratado como un paquete de Python.
    - **`v1/`**: Contiene la versión 1 de la API, lo que permite mantener diferentes versiones de la misma.
      - **`__init__.py`**: Similar al anterior, define este directorio como un paquete.
      - **`routes.py`**: Archivo donde se definen las rutas de la API y los controladores correspondientes.

  - **`core/`**: Contiene configuraciones y funcionalidades centrales de la aplicación.
    - **`__init__.py`**: Marca este directorio como un paquete.
    - **`config.py`**: Archivo para configuraciones generales de la aplicación (como claves, configuraciones de entorno, etc.).
    - **`security.py`**: Archivo para manejar autenticación y seguridad (puedes agregar funciones de seguridad, manejo de usuarios, etc.).

  - **`models/`**: Contiene las definiciones de los modelos de datos.
    - **`__init__.py`**: Indica que este directorio es un paquete.
  
  - **`repositories/`**: Encargado de la lógica de acceso a datos, como consultas a la base de datos.
    - **`__init__.py`**: Marca este directorio como un paquete.

  - **`schemas/`**: Define los esquemas de datos para la validación de entradas y salidas.
    - **`__init__.py`**: Indica que este directorio es un paquete.

  - **`services/`**: Contiene la lógica de negocio de la aplicación.
    - **`__init__.py`**: Indica que este directorio es un paquete.

  - **`main.py`**: El punto de entrada de la aplicación FastAPI. Aquí se inicia la aplicación y se incluyen las rutas.

  - **`database.py`**: (si se incluye la configuración de la base de datos) Este archivo contendrá la configuración para conectarse a la base de datos y definir las sesiones.

- **`requirements.txt`**: Archivo que lista las dependencias del proyecto, que pueden ser instaladas usando `pip`.

- **`README.md`**: Este archivo, que proporciona información sobre el proyecto, cómo usarlo y su estructura.

## Uso

1. **Clona este repositorio** o descarga el archivo del script.
  
2. **Ejecuta el script** en tu terminal:
   ```bash
   python script_name.py
3. Sigue las instrucciones en pantalla para proporcionar el nombre del proyecto y tus preferencias de configuración.
Requisitos
Python 3.x
FastAPI
SQLAlchemy (si eliges incluir configuración de base de datos)
Otras dependencias que se pueden definir en requirements.txt.
Contribuciones
Las contribuciones son bienvenidas. Si tienes sugerencias o mejoras, no dudes en abrir un issue o enviar un pull request.
