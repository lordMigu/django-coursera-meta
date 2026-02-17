# Clave primaria
En una base de datos relacional, cada tabla que representa una entidad tiene una columna que tiene un valor único para cada fila. Dicha columna o campo se conoce como Clave primaria. 

Si la Clave primaria de una tabla aparece como uno de los campos de otra tabla a la vez que tiene su propia Clave primaria, entonces se denomina Clave foránea.

Por ejemplo, en una tabla Productos, el campo ProductID es su clave primaria. 

En la tabla Clientes, el campo ProductID, que hace referencia al producto adquirido por el cliente, se convierte en la clave ajena.

La idea que subyace al diseño de tablas relacionadas es evitar la redundancia de datos, la repetición innecesaria de los mismos datos en muchas filas y garantizar la integridad de los datos.

Si el ProductID único de la tabla Clientes se sustituye por una convención de nomenclatura más larga para el campo de producto, habrá que introducirlo cada vez que un cliente compre el producto. Esto puede dar lugar a errores tipográficos.

Del mismo modo, si en la tabla de clientes se hace referencia al ID de un producto y se elimina, otros detalles del producto, como el precio, no estarán disponibles. 

Las bases de datos relacionales tienen un mecanismo para evitar la eliminación de la clave primaria si se está utilizando en la tabla relacionada, de modo que la integridad de los datos queda intacta.

Dado que los modelos de Django están mapeados a las tablas correspondientes en la base de datos, puedes definir una relación como esta entre los dos campos del modelo.

# Tipos de relaciones
Existen tres tipos de relaciones

* Uno-a-Uno,

* Uno-a-Muchos, y

* Muchos-a-Muchos.

Empecemos por la relación uno a uno.

## Relación uno a uno
Si existe una clave primaria en un modelo y sólo existe un registro en el otro modelo relacionado, se dice que los dos modelos tienen una relación uno a uno.

Utilicemos el ejemplo de un modelo de colegio y un modelo de director. Un colegio sólo puede tener un director o, dicho de otro modo, una persona sólo puede ser director de un colegio.

El modelo de colegio puede describirse como sigue:

```python
class college(Model): 
    CollegeID = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=50) 
    strength = models.IntegerField() 
    website=models.URLField() 
```

En el modelo de director, debe proporcionar el campo CollegeID como clave foránea. La opción on_delete especifica el comportamiento en caso de que se elimine el objeto asociado en el modelo principal. Los valores son:

* CASCADE: borra el objeto que contiene el campo ForeignKey

* PROTECT: Impide el borrado del objeto referenciado.

* RESTRICT: Impedir el borrado del objeto referenciado elevando RestrictedError

El modelo principal tiene la siguiente estructura de campos:
```python
class Principal(models.Model): 
    CollegeID = models.OneToOneField( 
                College, 
                on_delete=models.CASCADE 
                ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 
```
Cuando se ejecuta una migración en estos modelos, se crean las tablas respectivas con consultas SQL equivalentes:
```sql
CREATE TABLE "myapp_college" ("CollegeID" integer NOT NULL PRIMARY KEY, "name" varchar(50) NOT NULL, "strength" integer NOT NULL, "website" varchar(200) NOT NULL); 
```
```sql
CREATE TABLE "myapp_principal" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Qualification" varchar(50) NOT NULL, "email" varchar(50) NOT NULL, "CollegeID_id" integer NOT NULL UNIQUE REFERENCES "myapp_college" ("CollegeID") DEFERRABLE INITIALLY DEFERRED); 
```

Los valores posibles para on_delete se encuentran en django.db.models:

### CASCADE
Elimina en cascada. Django emula el comportamiento de la restricción SQL ON DELETE CASCADE y también elimina el objeto que contiene la clave foránea.

Model.delete() no se invoca en modelos relacionados, pero las señales pre_delete y post_delete se envían para todos los objetos eliminados.

### PROTECT
Evita la eliminación del objeto referenciado mediante la ejecución de ProtectedError, una subclase de django.db.IntegrityError.

### RESTRICT
Evita la eliminación del objeto referenciado mediante la ejecución de RestrictedError (una subclase de django.db.IntegrityError). A diferencia de PROTECT, se permite la eliminación del objeto referenciado si también hace referencia a un objeto diferente que se está eliminando en la misma operación, pero mediante una relación CASCADE.

Considere este conjunto de modelos:
```python
class Artist(models.Model):
    name = models.CharField(max_length=10)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)
'''    
El artista se puede eliminar incluso si esto implica eliminar un álbum referenciado por una canción, ya que la canción también referencia al artista mediante una relación en cascada. Por ejemplo:
''' 
>>> artist_one = Artist.objects.create(name="artist one")
>>> artist_two = Artist.objects.create(name="artist two")
>>> album_one = Album.objects.create(artist=artist_one)
>>> album_two = Album.objects.create(artist=artist_two)
>>> song_one = Song.objects.create(artist=artist_one, album=album_one)
>>> song_two = Song.objects.create(artist=artist_one, album=album_two)
>>> album_one.delete()
# Raises RestrictedError.
>>> artist_two.delete()
# Raises RestrictedError.
>>> artist_one.delete()
(4, {'Song': 2, 'Album': 1, 'Artist': 1})
```
>Consejo: Para asegurarte de estar dentro de la consola de Django, asegúrate de que los símbolos >>> estén al principio de tus comandos. A continuación, crea una variable e instancíala usando argumentos de palabra clave para la clase del modelo:
>
> `cat = DrinksCategory(category_name='coffee')`
>
>Finalmente, usa el método save() para guardar en la base de datos.
>
> `cat.save()`
>
> `fk = DrinksCategory.objects.get(pk=1)` # De esta manera puede obtener un registro de DrinksCategory

# Relación uno a muchos
En una relación Uno a Muchos, un objeto de un modelo puede asociarse a uno o más objetos de otro modelo. Por ejemplo, un profesor está cualificado para impartir una asignatura, pero puede haber más de un profesor en una universidad que imparta la misma asignatura.

El modelo de asignatura es el siguiente:
```python
class Subject(models.Model): 
    Subjectcode = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30) 
    credits = model.IntegerField() 
```
El modelo de profesor tiene su propia clave primaria. Tiene un `Foreignkey` que relaciona este modelo con el modelo de asignatura.
```python
class Teacher(models.Model): 
    TeacherID = models.IntegerField(primary_key=True) 
    subjectcode=models.ForeignKey( 
                Subject,  
                on_delete=models.CASCADE 
    ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 
```
Cuando ejecute la migración se ejecutarán las siguientes consultas SQL:
```sql
CREATE TABLE "myapp_subject" ("Subjectcode" integer NOT NULL PRIMARY KEY, "name" varchar(30) NOT NULL, "credits" integer NOT NULL, "Qualification" varchar(50) NOT NULL, "email" varchar(50) NOT NULL);

CREATE TABLE "myapp_teacher" ("TeacherID" integer NOT NULL PRIMARY KEY, "Qualification" varchar(50) NOT NULL, "email" varchar(50) NOT NULL, "subjectcode_id" integer NOT NULL REFERENCES "myapp_subject" ("Subjectcode") DEFERRABLE INITIALLY DEFERRED);

CREATE INDEX "myapp_teacher_subjectcode_id_bef86dea" ON "myapp_teacher" ("subjectcode_id");
```
# Relación Muchos-a-Muchos

En una relación Muchos-a-Muchos, múltiples objetos de un modelo pueden asociarse con múltiples objetos de otro modelo.

Redefinamos la relación entre los modelos de asignatura y profesor del ejemplo anterior. Si más de un profesor puede impartir la misma asignatura, un único profesor puede impartir más de una asignatura. Por lo tanto, hay una relación Many-to-Many entre los dos. Django implementa esto con un tipo de campo Many-to-Many. Vamos a utilizarlo en el modelo de asignatura.

El modelo de profesor es sencillo.
```python
class Teacher(models.Model): 
    TeacherID = models.IntegerField(primary_key=True) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 
```

El diseño de la clase Subject model refleja la relación Many-to-Many.
```python
class Subject(models.Model): 
    Subjectcode = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30) 
    credits = models.IntegerField() 
    teacher = models.ManyToManyField(Teacher)
``` 

Cuando se realicen las migraciones, se ejecutarán las siguientes consultas SQL para establecer una relación de muchos a muchos.
```sql
CREATE TABLE "myapp_teacher" ("TeacherID" integer NOT NULL PRIMARY KEY, "Qualification" varchar(50) NOT NULL, "email" varchar(50) NOT NULL);

CREATE TABLE "myapp_subject" ("Subjectcode" integer NOT NULL PRIMARY KEY, "name" varchar(30) NOT NULL, "credits" integer NOT NULL);

CREATE TABLE "myapp_subject_teacher" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "subject_id" integer NOT NULL REFERENCES "myapp_subject" ("Subjectcode") DEFERRABLE INITIALLY DEFERRED, "teacher_id" integer NOT NULL REFERENCES "myapp_teacher" ("TeacherID") DEFERRABLE INITIALLY DEFERRED);

CREATE UNIQUE INDEX "myapp_subject_teacher_subject_id_teacher_id_9b6a3c00_uniq" ON "myapp_subject_teacher" ("subject_id", "teacher_id");

CREATE INDEX "myapp_subject_teacher_subject_id_e87c76e7" ON "myapp_subject_teacher" ("subject_id");

CREATE INDEX "myapp_subject_teacher_teacher_id_359f8cce" ON "myapp_subject_teacher" ("teacher_id");
```
---
# related_name de ForeignKey() cambia el nombre de la columna?

No, el parámetro **`related_name`** en un `ForeignKey` **no cambia el nombre de la columna en la base de datos**.  

### Lo que hace realmente `related_name`
- Define el **nombre del atributo inverso** que se usará para acceder a los objetos relacionados desde el modelo opuesto.  
- Es decir, afecta cómo consultas en Django ORM, no cómo se crea la columna en SQL.

### Ejemplo
```python
class Autor(models.Model):
    nombre = models.CharField(max_length=100)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")
```

- En la base de datos, la tabla `Libro` tendrá una columna llamada `autor_id` (porque es la clave foránea).  
- El `related_name="libros"` significa que desde un objeto `Autor` puedes acceder a todos sus libros con:
  ```python
  autor = Autor.objects.get(id=1)
  autor.libros.all()   # gracias a related_name
  ```

### Sin `related_name`
Si no lo defines, Django usa por defecto `libro_set`:
```python
autor.libro_set.all()
```

### Resumen
- **Columna en DB:** siempre será `<nombre_campo>_id` (ej. `autor_id`).  
- **`related_name`:** solo cambia el nombre del atributo para acceder a la relación inversa en el ORM, no el esquema de la base de datos.
