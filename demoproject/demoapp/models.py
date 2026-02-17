from django.db.models import *

# Create your models here.

class Person(Model): 
    person_name = CharField(max_length=20) 
    email = EmailField() 
    phone = CharField(max_length=20)
    edad = IntegerField(null=True, blank=True)
    
    