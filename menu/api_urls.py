from django.urls import path
from . import views

app_name = 'menu-pizza'

urlpatterns = [
    path('GetPizzas', views.api_get_pizzas),
]