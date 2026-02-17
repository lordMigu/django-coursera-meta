# Manejo de errores en las vistas de Django

En el desarrollo web, es fundamental gestionar los errores de manera elegante para mejorar la experiencia del usuario (UX) y mantener la seguridad de la aplicación. Django ofrece varias herramientas para capturar y responder a situaciones inesperadas.

### Objetivos de aprendizaje

* Responder con estados de error HTTP (404, 500, etc.).
* Utilizar la excepción `Http404`.
* Configurar vistas y plantillas personalizadas para errores.

---

## 1. Subclases de HttpResponse

La forma más directa de devolver un error es retornar una instancia de una subclase de `HttpResponse`.

| Clase | Código de Estado | Uso |
| --- | --- | --- |
| `HttpResponseNotFound` | 404 | El recurso no existe. |
| `HttpResponseForbidden` | 403 | El usuario no tiene permiso. |
| `HttpResponseServerError` | 500 | Error interno del servidor. |
| `HttpResponseBadRequest` | 400 | La solicitud enviada es inválida. |

**Ejemplo:**

```python
from django.http import HttpResponseNotFound

def mi_vista(request):
    # Lógica de validación
    if not recurso_existe:
        return HttpResponseNotFound("<h1>Página no encontrada</h1>")

```

---

## 2. La excepción `Http404`

Django permite lanzar una excepción `Http404` en cualquier parte de la vista. Cuando se lanza, Django captura la excepción y devuelve la página de error 404 estándar del framework.

```python
from django.http import Http404
from .models import Producto

def detalle_producto(request, id):
    try:
        p = Producto.objects.get(pk=id)
    except Producto.DoesNotExist:
        raise Http404("El producto solicitado no existe")
    return render(request, 'detalle.html', {'producto': p})

```

---

## 3. Vistas de error personalizadas

Cuando `DEBUG = False` en tu archivo `settings.py`, Django buscará manejadores específicos en tu archivo `urls.py` principal para mostrar páginas personalizadas.

Puedes definir estas variables en tu `urls.py` global:

```python
# urls.py principal
handler404 = 'myapp.views.error_404'
handler500 = 'myapp.views.error_500'
handler403 = 'myapp.views.error_403'
handler400 = 'myapp.views.error_400'

```

### Plantillas predeterminadas

Si no quieres escribir una vista personalizada, simplemente puedes crear archivos HTML en tu carpeta de `templates` con los siguientes nombres:

* `404.html`
* `500.html`
* `403.html`
* `400.html`

Django los renderizará automáticamente cuando ocurra el error respectivo si el modo de depuración está desactivado.

---

## 4. Mejores Prácticas

* **DEBUG = False:** Asegúrate de desactivar el modo depuración en producción para que los usuarios no vean detalles técnicos o de seguridad (stack traces).
* **Logging:** Utiliza el sistema de registros de Django para guardar los errores 500 y analizarlos más tarde.
* **Mensajes claros:** Evita tecnicismos en las páginas 404; ofrece enlaces de regreso al inicio o un buscador.

---

## Resumen

Gestionar errores no se trata solo de evitar que la aplicación falle, sino de guiar al usuario cuando algo sale mal. Django facilita este proceso mediante excepciones integradas y un sistema de plantillas muy sencillo de configurar.
