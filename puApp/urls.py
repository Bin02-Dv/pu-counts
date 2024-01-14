from django.urls import path
from . import views

urlpatterns = [
    path('', views.datas_load, name='datas')
]