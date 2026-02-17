# La función **View** en Django

En Django, la **vista (view)** es uno de los componentes centrales dentro de la arquitectura **MVT (Modelo-Vista-Template)**.

Su papel principal es actuar como intermediaria entre:

* 🔹 El navegador (cliente)
* 🔹 El modelo (base de datos)
* 🔹 La plantilla (HTML que se muestra al usuario)

Cuando un usuario accede a una URL, el **despachador de URLs (urls.py)** analiza el patrón y ejecuta la función de vista correspondiente.

---

## ¿Qué hace una función view?

La función view:

1. Recibe una solicitud HTTP en forma de un objeto `HttpRequest`.
2. Procesa los datos enviados por el cliente.
3. Interactúa con el modelo si es necesario.
4. Devuelve una respuesta HTTP (`HttpResponse`) al navegador.

En términos simples:

> La view recibe datos, aplica lógica y devuelve una respuesta.

---

## Interacción con el Modelo

Aunque los modelos los estudiarás más adelante, es importante entender cómo la view trabaja con ellos.

Podemos decir que los modelos representan tablas de base de datos.
La view puede:

* 📖 Obtener datos (consultar registros)
* ➕ Crear nuevos registros
* ✏️ Actualizar registros
* ❌ Eliminar registros

Estas acciones suelen depender del método HTTP utilizado.

---

## Métodos HTTP: GET y POST

En Django, los métodos más comunes en una view son:

* **GET** → Para consultar o eliminar datos.
* **POST** → Para insertar o actualizar datos.

Ejemplo básico:

```python
from django.shortcuts import render

def myview(request):

    if request.method == 'GET':
        # Operación de lectura o eliminación

    if request.method == 'POST':
        # Operación de inserción o actualización
```

Si necesitas obtener datos enviados por el cliente:

```python
def myview(request):

    if request.method == 'GET':
        valor = request.GET['key']

    if request.method == 'POST':
        valor = request.POST['key']
```

---

## ¿Qué devuelve una view?

Toda función view debe devolver un objeto `HttpResponse`.

Este objeto contiene:

* El contenido (normalmente HTML)
* El tipo de contenido (`text/html` por defecto)
* El código de estado HTTP (200, 404, 500, etc.)
* Cabeceras adicionales

Sin embargo, en lugar de escribir HTML manualmente dentro de la respuesta, lo habitual es usar **plantillas (templates)**.

---

## Renderizado de Plantillas

La función `render()` facilita devolver una página HTML con datos dinámicos.

```python
from django.shortcuts import render

def myview(request):  

      if request.method=='GET':

      if request.method=='POST':  
            context={ } #dict que contiene datos a enviar al cliente  

      return render(request, 'mytemplate.html', context) 
```

Aquí:

* Django carga la plantilla `mi_template.html`
* Inserta los datos del diccionario `context`
* Devuelve el HTML generado al navegador

---

# Tipos de Views en Django

## 1️⃣ Function Based Views (FBV)

Son funciones normales de Python.

Ventajas:

* Simples
* Fáciles de entender al inicio
* Ideales para aprender Django

Desventaja:

* Pueden volverse repetitivas cuando la lógica crece

---

## 2️⃣ Class Based Views (CBV)

En lugar de usar una función, se crea una clase que hereda de `View`.

```python
from django.views import View
from django.http import HttpResponse

class MyView(View):

    def get(self, request):
        return HttpResponse("Respuesta GET")

    def post(self, request):
        return HttpResponse("Respuesta POST")
```

Ventajas:

* Separación clara entre métodos GET y POST
* Código más organizado
* Más reutilizable

---

## 3️⃣ Vistas Genéricas

Django ofrece vistas listas para usar en `django.views.generic`.

Algunas importantes:

* `TemplateView`
* `ListView`
* `DetailView`
* `CreateView`
* `UpdateView`

Estas permiten trabajar con modelos sin escribir toda la lógica manualmente.

Ejemplo conceptual:

```python
from django.views.generic import ListView
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = "productos/lista.html"
```

Aquí Django automáticamente:

* Consulta los objetos del modelo
* Los envía al template
* Renderiza la página

---

# Resumen

La view en Django:

* 🔹 Es el puente entre el usuario y la base de datos.
* 🔹 Procesa solicitudes HTTP.
* 🔹 Aplica lógica de negocio.
* 🔹 Devuelve una respuesta HTML mediante plantillas.
* 🔹 Puede implementarse como función, clase o vista genérica.

