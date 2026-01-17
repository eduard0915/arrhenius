from django.contrib import admin
from core.condition.models import Condition

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = (
        'zone_condition',
        'description_condition',
        'study_type',
        'temperture_sup',
        'temperture_inf',
        'percent_humidity_sup',
        'percent_humidity_inf',
        'period_minimum_time',
        'condition_enabled',
        'version',
        'date_creation'
    )
    list_filter = ('zone_condition', 'study_type', 'condition_enabled', 'date_creation')
    search_fields = (
        'zone_condition',
        'description_condition',
        'study_type'
    )
    readonly_fields = (
        'id',
        'user_creation',
        'date_creation',
        'user_updated',
        'date_updated'
    )
    fieldsets = (
        ('Información Básica', {
            'fields': (
                'zone_condition',
                'description_condition',
                'study_type',
            )
        }),
        ('Rangos de Operación', {
            'fields': (
                ('temperture_sup', 'temperture_inf'),
                ('percent_humidity_sup', 'percent_humidity_inf'),
                'period_minimum_time'
            )
        }),
        ('Detalles', {
            'fields': (
                'detail_condition',
            )
        }),
        ('Control de Versión', {
            'fields': (
                'version',
                'condition_enabled',
            )
        }),
        ('Auditoría', {
            'fields': (
                'id',
                'user_creation',
                'date_creation',
                'user_updated',
                'date_updated',
            ),
            'classes': ('collapse',)
        }),
    )
    ordering = ('-zone_condition', '-version')
    list_per_page = 25
    date_hierarchy = 'date_creation'
