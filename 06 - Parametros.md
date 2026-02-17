# Parámetro de ruta
El navegador del cliente envía datos junto con la propia URL. Por ejemplo, una URL como 
`http://example.com/customer/5` Aquí, el id del punto final de la URL, /customer/5, es el parámetro variable (puede ser cualquier otro número). 

El parámetro vinculado al punto final de la URL se denomina parámetro path. Tenga en cuenta que puede haber varios parámetros de ruta en la URL, separados por el símbolo `/`.

Por ahora, considere que el navegador utilizará la URL 
`http://localhost:8000/getuser/John/1`
 

El despachador de URL debe identificar a John como el parámetro `name` y a 1 como el parámetro `id`. 

Este patrón se asigna a la función `pathview()` con la siguiente ruta en la lista de patrones de URL del archivo url.py de la aplicación.
```python
path('getuser/<name>/<id>', views.pathview, name='pathview'), 
```
A continuación, añada la función `pathview()` en el archivo views.py.
```python
from django.http import HttpResponse 
def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id))
```

Como resultado, los parámetros de la URL anterior se analizan como parámetros name e id y son recogidos por la función pathview(), devolviendo la respuesta mostrada.

Una cosa importante que hay que entender aquí es que los parámetros añadidos dentro de la función path() en el archivo urls. py deben coincidir con los argumentos añadidos dentro de la función de vista pathview() asociada a ella en el archivo views.py. 

## Convertidores de ruta

El patrón URL trata los identificadores entre corchetes angulares (`<..>`) como los parámetros de la ruta. Por defecto, parsea el valor recibido al tipo cadena. Otros convertidores de ruta disponibles son:

* str - Coincide con cualquier cadena no vacía y excluye el separador de rutas,'`/`'. Este es el valor por defecto si no se incluye un convertidor en la expresión.

* int - Coincide con cero o cualquier número entero positivo y devuelve un int. Por ejemplo:/customer/`<int:id>`

* slug - Coincide con cualquier cadena slug formada por letras ASCII o números, incluidos los caracteres guión y guión bajo.

* uuid - Coincide con un UUID formateado. Por ejemplo: 075194d3-6885-417e-a8a8-6c931e272f00 y devuelve una instancia UUID.

* path - Coincide con cualquier cadena no vacía e incluye el separador de ruta, '/'.

# Parámetro de consulta
La URL del cliente puede contener una cadena de consulta vinculada al `/` final, por ejemplo 
`http://localhost:8000/getuser/?name=John&id=1`
 

Una cadena de consulta es una secuencia de uno o varios pares key=value concatenados por el símbolo `&`. Cada clave es el parámetro de consulta. La cadena de consulta termina con el símbolo `?` después del `/` final de la URL.

> Las cadenas de consulta son una alternativa a los parámetros de URL para añadir configuraciones de URL.

El despachador de URL no analiza estos parámetros. La vista los obtiene del objeto de solicitud que recibe. La propiedad `GET` del objeto `request` es un objeto diccionario. 

Los pares clave-valor de la cadena de consulta se añaden a la propiedad `request.GET`. De este modo, el nombre puede obtenerse con la expresión `request.GET['name']`.

>El siguiente paso es añadir la siguiente ruta en el archivo urls.py:
```python
path('getuser/', views.qryview, name='qryview') 
```
>Declare la función qryview en el archivo views.py.
```python
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 
```
Ahora, inicie el servidor y utilice como URL:

>```http://localhost:8000/myapp/?name=John&id=1```

El cliente obtiene de vuelta la respuesta mostrada:

>Name: John UserID: 1

# Parámetros del body

Un formulario HTML envía los datos a la URL mencionada en su atributo de acción utilizando el método POST. El método POST es una forma más segura de enviar datos que el método GET porque los datos no se revelan en la URL.

Construyamos un formulario sencillo que contenga dos elementos de entrada de texto. A continuación, guárdelo como form.html en la carpeta templates.
```html
<form action="/myapp/getform/" method="POST"> 
    {% csrf_token %} 
    <p>Name: <input type="text" name="id"></p> 
    <p>UserID :<input type="name" name="name"></p> 
    <input type="submit"> 
</form> 
```
>* La etiqueta `{% csrf_token %}` es necesaria para evitar ataques de falsificación entre sitios. Aprenderá más sobre esto más adelante en el curso.
>* La carpeta templates de este html debe ir en la ruta de la app.

A continuación, necesitará proporcionar una vista que renderice este formulario:
```python
def showform(request): 
    return render(request, "form.html") 
```
La lista de patrones de URL debe actualizarse utilizando la siguiente ruta:
```python
path("showform/", views.showform, name="showform"), 
```

El `http://localhost:8000/myapp/showform/` URL muestra un formulario al usuario.

Cuando usted lo envía, va a la dirección `http://localhost:8000/myapp/getform/`.* Ahora, asígnelo a la función `getform()` en el archivo urls.py.

> *Porque configuró `action="/myapp/getform/"` en el formulario
```python
path("getform/", views.getform, name='getform'),
```

Los datos del formulario que introduce el usuario pasan a formar parte del cuerpo de la solicitud. 

Por lo tanto, el atributo name de cada elemento del formulario se convierte en un parámetro del cuerpo y los datos introducidos se convierten en su valor. 

La función de vista pasa estos parámetros del cuerpo desde el atributo tipo diccionario de `request.POST`.
```python
def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))
``` 
Complete el formulario y envíelo. La función getform() devuelve los datos como respuesta.

En el mundo real, los datos recibidos pueden procesarse de forma significativa, como almacenarlos en una tabla de la base de datos. 

Aprenderá cómo hacerlo cuando explore Modelos, formularios y conexiones a bases de datos.

>* En esta lectura, ha aprendido acerca de los parámetros path, query y body, y cómo pasarlos y procesarlos utilizando diferentes métodos HTTP. 
>* Para manejar errores con HttpResponseNotFound  visite: https://docs.djangoproject.com/es/4.1/topics/http/views/
