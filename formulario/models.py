from django.db import models

# Create your models here.

class TransportForm(models.Model):
    date = models.DateField('Fecha')
    guide = models.CharField('Guía', max_length=50)
    patent = models.CharField('Patente', max_length=10)
    loading_station = models.CharField('Estación de carga', max_length=100)
    odometer = models.IntegerField('Odómetro')
    FUEL_TYPES = (
        ('diesel', 'Diesel'),
        ('bluemax', 'BlueMax'),
    )
    fuel_type = models.CharField('Tipo de combustible', max_length=10, choices=FUEL_TYPES)
    load_total = models.DecimalField('Total de carga', max_digits=10, decimal_places=2)
    image = models.ImageField('Imagen', upload_to='transport_forms/', blank=True, null=True)

    def __str__(self):
        return f"{self.guide} - {self.date}"

    class Meta:
        verbose_name = 'Formulario de Transporte'
        verbose_name_plural = 'Formularios de Transporte'
        ordering = ['-date']
