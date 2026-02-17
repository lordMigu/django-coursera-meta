from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index'),
    path('usuarios/<nombre>/<apellido>/<id>', views.paramRuta, name='paramRuta'),
    path('potencia/', views.paramConsulta, name='paramConsulta'),
    path("getform/", views.getform, name="getform"), 
    path("showform/", views.showform, name="showform"), 
]