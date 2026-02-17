El entorno virtual de Python se configura con la ayuda de un módulo incorporado llamado venv. Por ejemplo:

``` bash
python -m venv c:\Django 
C:\django>scripts\activate 
```

Una vez activado el entorno virtual, instale el framework Django con el siguiente comando:

``` bash
(django) c:\django> pip3 install django
```

El software VS Code puede iniciarse desde esta carpeta de la siguiente manera:  

``` bash
(django) C:\django>code . 
```

Asegúrese de que pip en instalado en su dispositivo. La última versión se puede instalar y actualizar mediante el comando:

``` bash
py -m pip install --upgrade pip
```

Puede crear un entorno virtual en el directorio específico del proyecto ejecutando el comando

``` bash
py -m venv env
```

*env es el nombre asignado al entorno virtual y esto creará una instalación virtual de Python en la carpetaenv.*

### Activar el entorno virtual

A continuación deberá activar el entorno virtual. Pondrá los ejecutables python y pip específicos del entorno virtual en el PATH de su shell.

Puede hacerlo ejecutando un comando como:

Windows

``` bash
.\env\Scripts\activate
```

Puede salir del entorno virtual ejecutando el comando
``` bash
deactivate
```

### Trabajar con laboratorios

Para ejecutar y ver su aplicación Django en el navegador, ejecute el siguiente comando en el terminal. (Verifique que se encuentra en el directorio donde reside el archivo manage.py)
``` bash
python3 manage.py runserver # To run the server
python3 manage.py makemigrations # To compile the migrations
python3 manage.py migrate  # To migrate the changes in Database
```