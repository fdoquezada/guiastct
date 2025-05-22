from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TransportForm(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('completed', 'Completado')
    ]
    
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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    status = models.CharField('Estado', max_length=20, default='pending', choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.id:  # Solo cuando se crea un nuevo registro
            self.created_by = kwargs.pop('created_by', None)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.guide} - {self.date}"

    class Meta:
        verbose_name = 'Formulario de Transporte'
        verbose_name_plural = 'Formularios de Transporte'
        ordering = ['-created_at']
