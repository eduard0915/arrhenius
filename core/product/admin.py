from django.contrib import admin
from core.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'code_product', 
        'description_product', 
        'type_prod', 
        'pharma_form', 
        'brand_product', 
        'version',
        'product_enabled',
        'date_creation'
    )
    list_filter = ('type_prod', 'product_enabled', 'pharma_form', 'date_creation')
    search_fields = (
        'code_product', 
        'description_product', 
        'brand_product', 
        'sanitary_license'
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
                'code_product',
                'description_product',
                'type_prod',
            )
        }),
        ('Detalles del Producto', {
            'fields': (
                'pharma_form',
                'brand_product',
                'sanitary_license',
                'image_product',
            )
        }),
        ('Control de Versión', {
            'fields': (
                'version',
                'product_enabled',
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
    ordering = ('-code_product', '-version')
    list_per_page = 25
    date_hierarchy = 'date_creation'
