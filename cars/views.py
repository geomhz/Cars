from django.shortcuts import render,redirect
from cars.models import Car
from cars.forms import CarModelForm

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

# Função serve tanto para o CarForm qto para o CarModelForm
def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', { 'new_car_form': new_car_form })


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

request.POST (para receber as infos do forms que cadastramos no new_car.html)
request.FILE (para receber as imagens do forms que cadastramos no new_car.html)

.save é a função que criamos no forms para salvar os dados no DB se o formulário for válido que enviamos pelo HTML
'''