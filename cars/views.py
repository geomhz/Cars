from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('brand__name')
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
    
    return render(
        request,
        'cars.html',
        {'cars': cars }
        )

'''
Cars.objects.all() # mesma coisa que o "SELECT * FROM xx" e retorna uma Queryset
    Executar uma query = executar uma consulta

Car.objects.filter(brand=1) # todos os carros da tabela Cars aplicando o filtro brand (por id sem especificar o name)

Car.objects.filter(brand__name='Chevrolet') # brand__name acessa o "name" da tabela Brand que é uma FK

Car.objects.filter(model__contains='C') # contains fitlra tudo que contém a escrita na coluna 'modelo'
Car.objects.filter(model__icontains='C') # icontains filtra ignorando as diferenças dos caracteres maiusc. minusc. 

search = request.GET.get('search') # Conseguimos fazer um filtro através da URL para renderizar o que o usuário quer
Car.objects.filter(model__contains=search).order_by('-brand__name') # "-" faz ordenar reversamente 

render pode ter parametros:
    request
    templates (.html)    
    context
'''