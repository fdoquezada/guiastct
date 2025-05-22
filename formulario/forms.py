from django import forms
from .models import TransportForm

class TransportFormForm(forms.ModelForm):
    class Meta:
        model = TransportForm
        fields = ['date', 'guide', 'patent', 'loading_station', 'odometer', 'fuel_type', 'load_total', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'guide': forms.TextInput(attrs={'class': 'form-control'}),
            'patent': forms.TextInput(attrs={'class': 'form-control'}),
            'loading_station': forms.TextInput(attrs={'class': 'form-control'}),
            'odometer': forms.NumberInput(attrs={'class': 'form-control'}),
            'fuel_type': forms.Select(attrs={'class': 'form-select'}),
            'load_total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'date': 'Fecha',
            'guide': 'Guía',
            'patent': 'Patente',
            'loading_station': 'Estación de carga',
            'odometer': 'Odómetro',
            'fuel_type': 'Tipo de combustible',
            'load_total': 'Total de carga',
            'image': 'Imagen',
        }
