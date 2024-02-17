from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from cars.models import Car
from cars.forms import CarModelForm

from django.views import View
from django.views.generic import ListView, CreateView

# Listando carros com CBVs
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    # Filtros + ordenação por brand e model
    def get_queryset(self):
        cars = super().get_queryset().order_by('brand__name', 'model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

# Registrando carros com CBVs
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'