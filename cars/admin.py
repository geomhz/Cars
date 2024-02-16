from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)

'''
list_display mostra todos os campos que temos disponiveis para visualização no painel do django admin
search_field é o campo de busca (filtro) que iremos buscar no painel do django admin

admin.site.register renderiza nosso models criado no painel do django admin ('127.0.0.1/admin')
'''