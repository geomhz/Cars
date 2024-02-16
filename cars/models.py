from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Tabela Car no banco de dados
class Car(models.Model):
    id = models.AutoField(primary_key=True) # id de chave primaria
    model = models.CharField(max_length=200) # modelo do carro
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # marca do carro
    factory_year = models.IntegerField(blank=True, null=True) # ano de fabricação
    model_year = models.IntegerField(blank=True, null=True) # ano do modelo
    plate = models.CharField(max_length=10, blank=True, null=True) # placa do carro
    value = models.FloatField(blank=True, null=True) # valor do carro
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.model

'''
Tipos de Campos
ForeignKey (recebe dados de outra tabela...Chave estrangeira)
AutoField (se autocompleta)
Charfield (campo de letras)
IntegerField (campo de números inteiros)
FloatField (campo de números com casas decimais)

Tipos de Parametros
primary_key (chave primaria) gera um id automático único
max_length=200 (max 200 caracteres)
blank=True (posso deixar em branco ao criar)
null=True (pode ser nulo)
on_delete=models.PROTECT (para deletar a marca do carro, precisamos primeiro deletar todos os carros da marca)
on_delete=models.CASCADE (se deletar a marca do carro todos os tipo Car da marca será deletado)
upload_to='cars/' (toda imagem que subir no servidor vai ser salvo na raiz cars/ do projeto) OBS: NECESSÁRIO MEDIA NO SETTINGS.PY + URLS STATIC + LIB PILLOW

Após criar o models de o comando no terminal para criar as tabelas no banco de dados:
python manage.py makemigrations
python manage.py migrate

No db criará NomeDaAplicação_NomeDaTabela, então aparecerá como cars_car

a função __str__ declaramos para retornar o modelo do carro no django admin
'''