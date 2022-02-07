from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('minha_consulta', views.review_consultation, name='minha_consulta'),
] 
