from django import forms
from .models import Car

class UserCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['vin', 'model', 'brand']
        labels = {
            'vin': 'VIN номер автомобиля',
            'model': 'Модель автомобиля',
            'brand': 'Марка автомобиля',
        }
        widgets = {
            'vin': forms.TextInput(attrs={
                'class': 'rectangle rectangle-1',
                'placeholder': 'VIN НОМЕР', 
                'style': 'font-size: 16px; text-align: center;'
                }),
            'model': forms.TextInput(attrs={
                'class': 'rectangle rectangle-1',
                'placeholder': 'МОДЕЛЬ АВТО', 
                'style': 'font-size: 16px; text-align: center;'
                }),
            'brand': forms.TextInput(attrs={
                'class': 'rectangle rectangle-1',
                'placeholder': 'МАРКА АВТО', 
                'style': 'font-size: 16px; text-align: center;'
                }),
        }