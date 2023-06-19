from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('fabricantes/', views.fabricantes, name='fabricantes'),
    path('fabricantes/detalhes/<int:id>', views.detalhes, name='detalhes'),
    path('fabricantes/add/', views.add, name='add'),
    path('fabricantes/add/addrecord/',views.addrecord, name='addrecord'),
    path('fabricantes/delete/<int:id>', views.delete, name='delete'),
]
