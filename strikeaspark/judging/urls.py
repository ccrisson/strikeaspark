from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('poster', views.poster, name='poster'),
    path('oral', views.oral, name='oral')
]
