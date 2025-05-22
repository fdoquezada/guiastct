from django.contrib import admin
from .models import TransportForm

class ImageFilter(admin.SimpleListFilter):
    title = 'Tiene imagen'
    parameter_name = 'has_image'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Sí'),
            ('no', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.exclude(image='')
        if self.value() == 'no':
            return queryset.filter(image='')

@admin.register(TransportForm)
class TransportFormAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'guide',
        'patent',
        'loading_station',
        'odometer',
        'fuel_type',
        'load_total',
        'has_image',
    )
    
    list_filter = (
        'date',
        'fuel_type',
        'patent',
        'loading_station',
        ImageFilter,
    )
    
    search_fields = (
        'guide',
        'patent',
        'loading_station',
    )
    
    ordering = ('-date',)
    
    date_hierarchy = 'date'
    
    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Tiene imagen'

    fieldsets = (
        ('Información Básica', {
            'fields': ('date', 'guide', 'patent')
        }),
        ('Detalles de Carga', {
            'fields': ('loading_station', 'odometer', 'fuel_type', 'load_total')
        }),
        ('Documentación', {
            'fields': ('image',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('date', 'guide', 'patent')
        return ()
