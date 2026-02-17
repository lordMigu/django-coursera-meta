# Añadir un objeto modelo con QuerySet

Cada atributo del modelo representa un campo de la base de datos.esencialmente se puede pensar en un modelo como un objeto Python, y los modelos ayudan a los desarrolladores a crear, leer, actualizar y eliminar objetos, comúnmente llamadas las operaciones CRUD.

Django tiene su propia capa ORM. Su mecanismo de migración propaga los modelos en tablas de bases de datos. 

Necesita construir un `QuerySet` a través de un Gestor de su clase de modelo para recuperar objetos de su base de datos.

El Customer.objects da el Gestor del modelo. Maneja todas las operaciones CRUD sobre la tabla de la base de datos. Por ejemplo, también se puede crear un objeto con el método create() de la siguiente manera:
```bash
>>> Customer.objects.create(name="Hameed") 
<Customer: Customer object (2)> 
```
El método create() realiza en realidad la operación INSERT de SQL.

Ahora, añadamos dos objetos al modelo Vehículo. Observe que uno de los campos del modelo Vehículo hace referencia a un objeto de la tabla Cliente como ForeignKey. Obtenga el objeto Cliente con una clave primaria = 2.
```bash
>>> from demoapp.models import Customer, Vehicle  
>>> c=Customer.objects.get(pk=2) 
>>> c.name 
'Hameed' 
```
Este objeto se utiliza como valor del atributo cliente en el objeto Vehículo.
```bash
>>> v=Vehicle(name="Honda", customer=c) 
>>> v.save() 
>>> v=Vehicle(name="Toyota", customer=c)   
>>> v.save() 
```
Del mismo modo, añada dos vehículos para el cliente "Enrique".
```bash
>>> c=Customer.objects.get(name="Henry") 
>>> Vehicle.objects.create(name="Ford", customer=c) 
<Vehicle: Vehicle object (3)> 
>>> Vehicle.objects.create(name="Nissan", customer=c) 
<Vehicle: Vehicle object (4)> 
```

# Obtener objetos del modelo
Un QuerySet representa una colección de objetos de su base de datos. Representa una consulta a SELECT. Para recuperar todos los objetos, utilice el método all() del Gestor.
```bash
>>> model.objects.all()
```

El método all() devuelve una lista de objetos. Puede iterar sobre ella con la técnica habitual de bucle for o de comprensión de listas.
```bash
>> lst=Customer.objects.all()  
>>> [c.name for c in lst] 
['Henry', 'Hameed'] 
```
Puede aplicar filtros a los datos obtenidos del modelo. Esto se utiliza para obtener objetos que satisfagan los criterios dados. En términos SQL, una QuerySet equivale a una sentencia SELECT, es como aplicar una cláusula WHERE.
```bash
model.objects.filter(criteria) 
```

Por ejemplo, utilice la siguiente sentencia para recuperar todos los clientes cuyos nombres empiecen por 'H'.

`mydata = Customer.objects.filter(name__startswith='H') `

Del mismo modo, puede recuperar los objetos del modelo Vehículo. Recuerde que el objeto Vehículo hace referencia a un objeto cliente. Puede recuperar los atributos del cliente relacionado de la siguiente manera:
```bash
>>> lst=Vehicle.objects.all() 
>>> for v in lst: 
...     print (v.name, " : ", v.customer.name) 
...  
Honda :  Hameed 
Toyota :  Hameed 
Ford :  Henry 
Nissan :  Henry 
```

# Actualizar y eliminar un objeto del modelo
Para actualizar un objeto, como cambiar el nombre del cliente de Henry a Helen, asigne un nuevo valor al atributo name y guarde.
```bash
>>> c=Customer.objects.get(name="Henry") 
>>> c.name="Helen" 
>>> c.save() 
```
Del mismo modo, el método delete() del gestor de modelos elimina físicamente la fila correspondiente en la tabla asignada del modelo.
```bash
>>> c=Customer.objects.get(pk=4) 
>>> c.delete() 
(1, {'demoapp.Customer': 1}) 
```

De este modo, puede realizar las operaciones CRUD en una tabla de la base de datos utilizando la API QuerySet en lugar de ejecutar consultas SQL sin procesar.