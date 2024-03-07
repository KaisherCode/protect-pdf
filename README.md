# Cómo proteger con contraseña archivos PDF con código Python

Para automatizar el generador de contraseña para archivos PDF:

1. Abrir el terminal y Crear el nombre del proyecyo `mkdir protect-pdf` Luego ingresar al proyecto con `cd protect-pdf`

    - Crear entorno virtual `python3 venv venv`
    - Activar el entorno virtual `source venv/bin/activate`. Y para desactivar `deactivate`.

2. Dentro del directorio `protect-pdf` Crear un archivo llamado `password_setting.csv` en donde vamos a establecer la contraseñas para cada una de nuestros archivos PDF. El archivo debe tener encabezados [Ruta y Clave]

3. Crear el directorio llamado certificadosPDF `mkdir certificadosPDF` y está debe contener los archivos PDF sin contraseña.

4. Crear el directorio llamado protectedPDF `mkdir protectedPDF` Aquí se crearan los archivos PDF protegido con contraseña.

5. Inicializar git `git init`

6. Abrir el proyecto en Visual Studio Code `code .`

7. Instalar pandas `pip install pandas`

8. Instalar pyPDF2 `pip install pypdf2` 

9. Crear el archivo protect_pdf.py `touch protect_pdf.py`





