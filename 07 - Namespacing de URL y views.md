En cada app, hay un archivo urls.py que define la lista de patrones de URL para esa app. Cada patrón se construye mediante la función django.urls.path(). Sus argumentos son una cadena de ruta URL, el nombre de la función de views que se le va a asignar y un nombre de argumento opcional.
A continuación se muestra urls.py de una app:
```python
#demoapp/urls.py 
from django.urls import path 
from . import views 

  urlpatterns = [ 
    path('', views.index, name='index'), 
    path('login/', views.login, name='login') 
] 
```
Se incluye en el urlpatterns del proyecto.
```python
from django.contrib import admin 
from django.urls import path, include 

  urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('demo/', include('demoapp.urls')), 
]
```

# función reverse()
Sin embargo, las URL codificadas de forma rígida hacen que la aplicación sea menos escalable y difícil de mantener a medida que crece el proyecto. En tal caso, puede obtener la URL a partir del parámetro de nombre utilizado en la función path().

Inicie el shell de Django.
```shell
python manage.py shell 
```

La función reverse() de Django devuelve la ruta URL a la que está asignada.
```shell
>>> from django.urls import reverse 
>>> reverse('index') 
'/demo/' 
```

El problema surge cuando la función de vista del mismo nombre se define en más de una aplicación. Aquí es donde se necesita la idea de un **namespace**.

# Namespacing la app

El namespacing de la aplicación se crea definiendo la variable app_name en el urls.py de la aplicación y asignándole el nombre de la app. En el script demoapp/urls.py, realice el cambio utilizando el siguiente código:
```python
#demoapp/urls.py
from django.urls import path  
from . import views    
app_name='demoapp' 
urlpatterns = [  
    path('', views.index, name='index'),      
] 
```

app_name define el namespacing de la aplicación para que las vistas de esta app se identifiquen con él.

Para obtener la ruta URL de la función index(), llame a la función reverse() anteponiéndole el namespace.
```shell
>>> reverse('demoapp:index') 
'/demo/' 
```
Para apreciar la ventaja de definir un namespace, añada otra app en el proyecto, por ejemplo, **newapp**. Proporcione una función de vista index() en ella y defina `app_name` en su archivo URLConf (es decir urls.py).
```python
#newapp/urls.py 
from django.urls import path 
from . import views 
app_name='newapp' 
urlpatterns = [ 
    path('', views.index, name='index'), 
]
```
Actualice el urls.py del proyecto.
```python
from django.contrib import admin 
from django.urls import path, include 

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('demo/', include('demoapp.urls')), 
    path('newdemo/', include('newapp.urls')), 
] 
```
La función reverse() se ejecuta para la view index en el namespace *newapp*.
```shell
>>> reverse('newapp:index') 
'/newdemo/'
```

Puede ver que Django diferencia entre URLs con el mismo nombre en múltiples apps con namespaces de app.

# Namespace de instancia

También puede utilizar el parámetro namespace en la función `include()` al añadir el urlpattern de una app al de un proyecto.
```python
#in demoproject/urls.py 
urlpatterns=[ 
    # ... 
    path('demo/', include('demoapp.urls', namespace='demoapp')), 
    # ... 
] 
```

Este namespace se denomina `instance namespace`.

## Uso del namespace en los view

Supongamos que desea que el usuario sea redirigido condicionalmente a la vista de inicio de sesión desde dentro de otra vista. Necesita obtener la URL de la vista de inicio de sesión y enviar el control a ella con `HttpResponsePermanentRedirect`.
```python
from django.http import HttpResponsePermanentRedirect 
from django.urls import reverse 
  
def myview(request): 
    .... 
    return HttpResponsePermanentRedirect(reverse('demoapp:login'))
```

## namespace en la etiqueta url 
Se enviará un formulario HTML a la URL especificada en el atributo action.
```html
<form action="/demoapp/login" method="post"> 

#form attributes 

<input type='submit'> 

</form> 
```
A continuación, el formulario será procesado por la vista asignada a esta URL. Sin embargo, como se mencionó anteriormente, no se desea una URL codificada. En su lugar, utilice la etiqueta url del lenguaje de plantillas Django. Devuelve la ruta absoluta de la URL nombrada.

Utilice la etiqueta url para obtener la ruta de la URL de forma dinámica, como se muestra a continuación:
```html
<form action="{% url 'login' %}" method="post"> 
#form attributes 
<input type='submit'> 
</form> 
```

De nuevo, la vista de inicio de sesión puede estar presente en varias aplicaciones. Utilice la URL nombrada cualificada con el espacio de nombres para resolver el conflicto.

```html
<form action="{% url 'demoapp:login' %}" method="post"> 
#form attributes 
<input type='submit'> 
</form> 
```
El concepto de espacio de nombres ayuda a resolver el conflicto que surge cuando varias aplicaciones de un mismo proyecto tienen vistas con el mismo nombre.

Usted ha cubierto algunos de los conceptos aquí en línea con el uso de plantillas de formulario en Django. Si tiene dificultades para entender algunas cosas, tenga la seguridad de que será mucho más claro una vez que cubra el tema de las plantillas en este curso.

En esta lectura, ha explorado más a fondo el concepto de URL Namespacing y Views en Django. 

---

Mas informacion:

[Expresiones regulares](https://docs.djangoproject.com/en/4.1/topics/http/urls/#using-regular-expressions)