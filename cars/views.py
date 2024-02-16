from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all() # mesma coisa que o "SELECT * FROM xx"

    return render(
        request,
        'cars.html',
        {'cars': {'model': 'Ferrari GTB'} }
        )

'''
Cars.objects.all() # mesma coisa que o "SELECT * FROM xx" e retorna uma Queryset

render pode ter parametros:
    request
    templates (.html)    
    context
'''