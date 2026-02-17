La opción del comando **startapp** del script manage.py crea una estructura de carpetas por defecto para la app de ese nombre.

He aquí cómo crear un demoapp en la carpeta demoproject.

``` bash
(djenv) C:\djenv\demoproject>python manage.py startapp demoapp
```
Se crea una carpeta con el nombre de la app dentro de la carpeta padre. Contiene algunos scripts Python. La estructura de la carpeta tiene este aspecto:

``` bash
C:\djenv\demoproject 
│   db.sqlite3 
│   manage.py 
│ 
├───demoapp 
│   │   admin.py 
│   │   apps.py 
│   │   models.py 
│   │   tests.py 
│   │   views.py 
│   │   __init__.py 
│   │ 
│   └───migrations  #carpeta
│           __init__.py 
│ 
└───demoproject 
    │   asgi.py 
    │   settings.py 
    │   urls.py 
    │   wsgi.py 
    │   __init__.py
```

## views.py

En Django, una views es una función definida por el usuario que se llama cuando el despachador de URL de Django identifica la URL de solicitud del cliente y la hace coincidir con un patrón de URL definido en el archivo urls.py.

El archivo de vistas autocreado está vacío al principio.

Añadamos en él una función de vista llamada index() guardando el siguiente fragmento.
``` python
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 
```
## urls.py

El paquete del proyecto tiene un archivo con este nombre que define los patrones de URL para el proyecto.

En una línea similar, necesita proporcionar el mecanismo de enrutamiento de URL para la aplicación.

Una cosa importante a tener en cuenta aquí, a diferencia del vídeo que ha visto antes, es que el  archivourls.py puede configurarse tanto a nivel de proyecto como de aplicación. En el ejemplo siguiente, el urls.py se configurará tanto a nivel de proyecto como de app.

La carpeta app no tiene un archivo con este nombre cuando se crea. Por lo tanto, deberá crear uno.

Guarde el siguiente fragmento como urls.py en la carpeta demoapp.
``` python
from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index'), 
] 
```
A continuación, deberá actualizar la lista urlpatterns en el urls.py de la carpeta del proyecto e incluir las configuraciones de URL de la app.

El demoproject/urls.py actualizado debería tener este aspecto:
``` python
from django.contrib import admin 
from django.urls import include, path 

urlpatterns = [ 
    path('demo/', include('demoapp.urls')), 
    path('admin/', admin.site.urls), 
]
```

## models.py
En este archivo se crean los modelos de datos necesarios para el procesamiento en esta app. Por defecto está vacío. Un modelo de datos es una clase Python basada en django.db.modelsclass. Todos los modelos presentes aquí se migran a las tablas de la base de datos. Por ahora, deje su archivo tal como está sin añadir ningún modelo. Más adelante aprenderá a trabajar con modelos.

# Actualizar settings.py

Por último, debe actualizar la lista de INSTALLED_APPS en el archivo de configuración del proyecto. Esta lista ya contiene algunas aplicaciones preinstaladas. Añada el nombre de 'demoapp' para que tenga este aspecto:
``` python
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth',  
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'demoapp', 
] 
```

Después de realizar los pasos explicados anteriormente, ejecute el servidor de desarrollo con Django ```python manage.py runserver``` y visite ```localhost:8000/demo/``` en el navegador.