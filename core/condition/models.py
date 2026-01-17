import uuid
from core.models import BaseModel
from django.db import models
from crum import get_current_user
from studystb.settings import MEDIA_URL, STATIC_URL


# Productos
class Condition(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    zone_condition = models.CharField(max_length=10, verbose_name='Zona')   
    description_condition = models.CharField(max_length=100, verbose_name='Descripción')     
    study_type = models.CharField(max_length=20, verbose_name='Tipo de estudio')
    temperture_sup = models.SmallIntegerField(verbose_name='Temp. Superior °C')     
    temperture_inf = models.SmallIntegerField(verbose_name='Temp. Inferior °C')
    percent_humidity_sup = models.SmallIntegerField(verbose_name='% de HR superior')     
    percent_humidity_inf = models.SmallIntegerField(verbose_name='% de HR inferior')  
    period_minimum_time = models.SmallIntegerField(verbose_name='Meses del Estudio')
    detail_condition = models.TextField(verbose_name='Detalle de la condición', null=True, blank=True)   
    version = models.PositiveSmallIntegerField(default=1)
    condition_enabled = models.BooleanField(default=True, verbose_name='Activo')
    
    def __str__(self):
        return self.zone_condition
    
    class Meta:
        db_table = 'Condition'
        verbose_name = 'Condition'
        verbose_name_plural = 'Conditions'
        ordering = ['zone_condition', '-version']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs):
        user = get_current_user()
        if user:
            if not self.user_creation:
                self.user_creation = user
            else:
                self.user_updated = user        
        return super(Condition, self).save(*args, **kwargs)
