from django import forms
from .models import TransportForm

class TransportFormForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=TransportForm.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select status-select'}),
        required=False
    )

    class Meta:
        model = TransportForm
        fields = [
            'date', 
            'guide', 
            'patent', 
            'loading_station', 
            'odometer', 
            'fuel_type', 
            'load_total', 
            'image',
            'status'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'guide': forms.TextInput(attrs={'class': 'form-control'}),
            'patent': forms.TextInput(attrs={'class': 'form-control'}),
            'loading_station': forms.TextInput(attrs={'class': 'form-control'}),
            'odometer': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'fuel_type': forms.Select(attrs={'class': 'form-select'}),
            'load_total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
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
            'status': 'Estado'
        }

    def clean_odometer(self):
        odometer = self.cleaned_data.get('odometer')
        if odometer is not None and odometer < 0:
            raise forms.ValidationError('El número de odómetro debe ser positivo')
        return odometer

    def clean_load_total(self):
        load_total = self.cleaned_data.get('load_total')
        if load_total is not None and load_total < 0:
            raise forms.ValidationError('El total de carga debe ser positivo')
        return load_total

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5242880:  # 5MB en bytes
                raise forms.ValidationError('La imagen debe ser menor a 5MB')
            if not image.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                raise forms.ValidationError('Formato de imagen no válido. Solo se aceptan JPG, PNG y GIF')
        return image
