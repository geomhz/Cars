from django import forms
from cars.models import Brand, Car

# Usando o ModelForm já utiliza todo o nosso models automático
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo: R$20.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Ano mínimo: 1975')
        return factory_year

'''
# CarForm da maneira manual de se fazer, ligada com a views manual que vou deixar comentado
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )

        car.save()
        return car
'''

'''
Criando um formulário para o usuário preencher (todos campos que temos em models,
que é o campo que precisamos captar as informações para adicionar um novo registro)

está salvando o que foi passado no CarForm para o Car do models (para salvar no db)

funções com clean_ na frente significa funções de validação de campos
'''