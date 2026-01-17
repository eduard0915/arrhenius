import uuid
from core.models import BaseModel
from django.db import models
from crum import get_current_user
from studystb.settings import MEDIA_URL, STATIC_URL


# Productos
class Product(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    code_product = models.CharField(max_length=25, verbose_name='Código')
    description_product = models.CharField(max_length=200, verbose_name='Descripción Genérica')
    pharma_form = models.CharField(max_length=80, verbose_name='Forma Farmacéutica', null=True, blank=True)
    type_prod = models.CharField(max_length=100, verbose_name='Tipo de Producto')
    brand_product = models.CharField(
        default='No aplica', max_length=80, verbose_name='Nombre Comercial', null=True, blank=True)
    sanitary_license = models.CharField(max_length=80, verbose_name='Registro Sanitario')
    version = models.PositiveSmallIntegerField(default=1)
    product_enabled = models.BooleanField(default=True, verbose_name='Activo')
    image_product = models.ImageField(upload_to='product/images/', null=True, blank=True)
    
    def __str__(self):
        na_list = ['No Aplica', 'NA', 'N/A']
        if self.brand_product in na_list:
            self.brand_product = 'No aplica'
        if self.pharma_form:
            if not self.brand_product == 'No aplica':
                return f'{self.code_product} {self.description_product} {self.pharma_form} - {self.brand_product}'
            else:
                return f'{self.code_product} {self.description_product} {self.pharma_form}'
        else:
            if not self.brand_product == 'No aplica':
                return f'{self.code_product} {self.description_product} - {self.brand_product}'
            else:
                return f'{self.code_product} {self.description_product}'

    def get_image(self):
        if self.image_product:
            return '{}{}'.format(MEDIA_URL, self.image_product)
        return '{}{}'.format(STATIC_URL, 'lib/now-ui-dashboard-pro-v1.6.0/assets/img/image_placeholder.jpg')

    class Meta:
        db_table = 'Product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-code_product', '-version']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs):
        user = get_current_user()
        if user:
            if not self.user_creation:
                self.user_creation = user
            else:
                self.user_updated = user
        self.code_product = self.code_product.upper()
        return super(Product, self).save(*args, **kwargs)
