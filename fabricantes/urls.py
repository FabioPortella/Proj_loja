from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('fabricantes/', views.fabricantes, name='fabricantes'),
    path('fabricantes/detalhes/<int:id>', views.detalhes, name='detalhes'),
]
