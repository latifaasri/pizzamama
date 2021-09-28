from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
from django.core import serializers

# Create your views here.
#Exercice
#Les pizzas : pepina : 8.5, cannibale : 11.0 , carnivore : 12.5 , 4 frommages : 11.5


def index(request):
    '''pizzas = Pizza.objects.all()
    pizzas_names_and_prices = [pizza.nom + " : " +str(pizza.prix) + "€" for pizza in pizzas]
    pizzas_names_str = ", ".join(pizzas_names_and_prices)
    return HttpResponse("Les pizzas : " + pizzas_names_str)'''

    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas': pizzas})

def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)

