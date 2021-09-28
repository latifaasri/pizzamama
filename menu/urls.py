from django.urls import path
from . import views

app_name = 'menu-pizza'

urlpatterns = [
    path('', views.index, name="index"),

]