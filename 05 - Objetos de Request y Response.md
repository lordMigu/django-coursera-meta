## Objetos de **request** y **response**

Una aplicación web funciona bajo el principio de un ciclo de **request-response** en una arquitectura cliente-servidor, siguiendo el protocolo HTTP.

Generalmente, un navegador envía la **request** en forma de URL. La aplicación web genera una **response** adecuada basándose en los datos contenidos en dicha **request**.

Django gestiona este proceso mediante las clases `HttpRequest` y `HttpResponse` del módulo `django.http`.

### El flujo en Django

1. Django obtiene el objeto `HttpRequest` del contexto proporcionado por el servidor.
2. Cuando se recibe una **request** de un cliente, el despachador de URL de Django invoca una vista que coincida con el patrón.
3. Se pasa este objeto `HttpRequest` como primer argumento, permitiendo que todos los metadatos de la **request** estén disponibles para la vista.

---

### Objeto `HttpRequest`

El objeto de **request** se define por sus atributos y métodos, fundamentales para la lógica de cualquier vista en Django.

* **`request.method`**: Identifica cómo se ha dirigido el cliente al servidor (GET, POST, PUT, DELETE).
```python
if request.method == 'GET': 
    do_something() 
elif request.method == 'POST': 
    do_something_else() 

```


* `request.GET` y `request.POST`: Diccionarios que contienen los parámetros enviados en la **request**.
* **`request.COOKIES`**: Diccionario con las cookies enviadas por el navegador.
* **`request.FILES`**: Contiene los archivos subidos mediante formularios multipart.
* **`request.user`**: Representa al usuario actual. Si no está autenticado, devuelve `AnonymousUser`.
```python
if request.user.is_authenticated(): 
    # Lógica para usuarios logueados
else: 
    # Lógica para usuarios anónimos

```

* `request.has_key()`: Se trata de un método disponible para el objeto de solicitud. Ayuda a comprobar si el diccionario de parámetros GET o POST tiene un valor para la clave dada.

---

### Objeto `HttpResponse`

A diferencia del `HttpRequest` (que viene del servidor), el objeto de **response** se instancia dentro de la función de la vista antes de ser devuelto al cliente.

> **Nota:** Aunque puedes devolver HTML puro ("hardcoded"), lo ideal es usar el sistema de plantillas de Django.

**Ejemplo básico:**

```python
from django.http import HttpResponse 

def index(request): 
    return HttpResponse("Hello World") 

```

**Ejemplo con plantillas:**

```python
from django.http import HttpResponse 
from django.template import loader 

def index(request): 
    template = loader.get_template('demoapp/index.html') 
    context = {}  
    return HttpResponse(template.render(context, request)) 
```

#### Atributos principales de `HttpResponse`:

| Atributo/Método | Descripción |
| --- | --- |
| **`status_code`** | Devuelve el código de estado HTTP de la **response**. |
| **`content`** | Devuelve la cadena de bytes del contenido. |
| **`__getitem__()`** | Método que devuelve el valor de una cabecera. |
| **`__setitem__()`** | Permite añadir una cabecera. |
| **`write()`** | Crea un objeto similar a un archivo para escritura directa. |

---

### Ejemplo práctico: Inspeccionando la **request**

Puedes crear una vista simple en `views.py` para visualizar los datos que viajan en la **request**:

```python
from django.http import HttpResponse 

def index(request): 
    path = request.path 
    method = request.method 
    content = ''' 
    <center>
        <h2>Testing Django Request Response Objects</h2> 
        <p>Request path: {}</p>
        <p>Request Method: {}</p>
    '''.format(path, method) # igual q {path} o {method} con f''' ... '''
    return HttpResponse(content) 

```

Al iniciar el servidor y acceder a `http://localhost:8000/demo/`, verás la **response** generada dinámicamente con los datos de tu navegación.
