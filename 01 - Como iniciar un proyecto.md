Un proyecto Django es un paquete Python que contiene la configuración de la base de datos utilizada por varios sub-módulos (Django los llama apps) y otras configuraciones específicas de Django.

### startproject
Utilice el comando **startproject** de Django-admin como se indica a continuación:  

``` bash
(djenv) C:\djenv>django-admin startproject demoproject
```

startproject es la plantilla de proyecto por defecto de Django. Crea la siguiente estructura de archivos en el entorno Python:

``` python
C:\djenv\demoproject 
│   manage.py 
│ 
└───demoproject 
        asgi.py 
        settings.py 
        urls.py 
        wsgi.py 
        __init__.py    
```

### startapp

Como se mencionó anteriormente, una carpeta de proyecto Django puede contener una o más apps. Una app también está representada por una carpeta de un sistema de archivos específico. El comando para crear una app es:
``` bash
python manage.py startapp <name of app>
```
Explorará la estructura de una app más adelante.

> Se puede usar ```django-admin starapp <name of app>``` sin embargo esto crearía una app dentro de tu ubicacion actual. Cuando se trabaja con múltiples archivos de configuración en proyectos Django, se prefiere django-admin sobre manage.py para ejecutar los comandos Django en la línea de comandos. 

### makemigrations

Django gestiona las operaciones de base de datos con la técnica ORM. La migración se refiere a generar una tabla de base de datos cuya estructura coincida con el modelo de datos declarado en la app. 

El siguiente comando debe ejecutarse siempre que se declare un nuevo modelo.
``` bash
python manage.py makemigrations
```

### migrate

Esta opción del comando manage.py sincroniza el estado de la base de datos con los modelos y migraciones actualmente declarados.
``` bash
python manage.py migrate
```

### runserver

Este comando inicia el servidor de desarrollo incorporado de Django en la máquina local con la dirección IP 127.0.0.1 y el puerto 8000.
``` bash
python manage.py runserver
```

### Shell

Este comando abre una shell Python interactiva dentro del proyecto. Esto es útil cuando se requiere realizar algunas operaciones interactivas rápidas.
``` bash
python manage.py shell
```

## Estructura del proyecto

La plantilla startproject coloca cuatro archivos más en la carpeta del paquete.

#### settings.py

Django configura parámetros específicos con sus valores por defecto y los coloca en este archivo. 

La utilidad django-admin y el script **manage.py** utilizan estos ajustes al realizar diversas tareas administrativas.

### urls.py

Este script contiene una lista de objetos urlpatterns. Cada vez que el navegador del cliente solicita una URL, el servidor Django busca que coincida con su patrón y dirige la solicitud a la vista mapeada. 

La estructura por defecto de urls.py contiene una vista mapeada al sitio Admin del proyecto.
``` python
from django.contrib import admin 
from django.urls import path 

 urlpatterns = [ 
    path('admin/', admin.site.urls), 
] 
```
### asgi.py

Este archivo es utilizado por los servidores de aplicaciones que siguen el estándar ASGI para servir aplicaciones web asíncronas.

### wsgi.py

Muchos servidores de aplicaciones web implementan el estándar WSGI. Este script es el punto de entrada para que dichos servidores compatibles con WSGI sirvan su aplicación web clásica.

---
# settings.py

Este archivo define los atributos que influyen en el funcionamiento de una aplicación Django. La plantilla startproject asigna algunos valores por defecto a estos atributos. Pueden modificarse según las necesidades durante el uso de la aplicación.

Vamos a explicar algunos ajustes críticos.

### INSTALLED_APPS

Se trata de una lista de cadenas. Cada cadena representa la ruta de una app dentro de la carpeta padre del proyecto. La plantilla startproject instala algunas apps por defecto. Aparecen en la lista INSTALLED_APPS.

``` python
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
] 
```

Esta lista debe actualizarse añadiendo su nombre cada vez que se instale una nueva app. 

Por ejemplo, si creamos un demoapp con el siguiente comando:
``` bash
python manage.py startapp demoapp
```

A continuación, **añada la cadena 'demoapp' dentro de la lista INSTALLED_APP.**

``` python
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'demoapp', # Agregelo
] 
```
### Bases de datos

Este atributo es un diccionario que especifica la configuración de una o más bases de datos a utilizar por la aplicación Django actual. Por defecto, Django utiliza la base de datos SQLite. Por lo tanto, este ajuste tiene una configuración predefinida para ella.
``` python
DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / 'db.sqlite3', 
    } 
} 
```
En lugar de SQLite, puede optar por utilizar cualquier otro. Por ejemplo, para MySQL, la configuración de la base de datos podría ser la siguiente:
``` python
DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'djangotest',   
        'USER': 'root',   
        'PASSWORD': 'password',   
        'HOST': '127.0.0.1',   
        'PORT': '3306',            
    }   
} 
```

### DEBUG = Verdadero

Por defecto, el servidor de desarrollo se ejecuta en modo de depuración. Esto ayuda a desarrollar la aplicación ya que el servidor recoge los cambios en el código y la salida puede ser refrescada sin reiniciar. Sin embargo, **debe desactivarse en el entorno de producción.**

### ALLOWED_HOSTS

Este atributo es una lista de cadenas. Por defecto, está vacía. Cada cadena representa el host/dominio completamente cualificado donde este sitio Django puede ser servido. Por ejemplo, para hacer que el sitio que se ejecuta en localhost sea visible externamente, puede añadir 0.0.0.0:8000 a esta lista.

### ROOT_URLCONF

Este ajuste es una cadena que apunta al módulo urls.py en el que se encuentran los patrones de URL del proyecto. En este caso, sería
``` python
ROOT_URLCONF = 'demoproject.urls'
```

### STATIC_URL

Este ajuste apunta a la carpeta en la que se colocan los archivos estáticos, como el código JavaScript, los archivos CSS y las imágenes. Normalmente, se establece en 'static/' que corresponde a la carpeta de este nombre en la carpeta padre del proyecto.
``` python
STATIC_URL = 'static/'
```
---
# Pruebe la instalación

Después de crear el proyecto, para verificar que se ha construido correctamente, inicie el servidor de desarrollo con el siguiente comando mientras permanece en la carpeta padre del proyecto:
``` bash
python manage.py runserver
```

