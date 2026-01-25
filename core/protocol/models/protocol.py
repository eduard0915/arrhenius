import uuid
from django.db import models
from django.conf import settings
from core.models import BaseModel
from core.condition.models import Condition


class Protocol(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    code_protocol = models.CharField(max_length=50, unique=True, verbose_name='Código de Protocolo')
    study_type = models.CharField(max_length=100, verbose_name='Tipo de Estudio')
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='protocols', verbose_name='Condición')
    objective = models.TextField(verbose_name='Objetivo')
    numbers_batch = models.PositiveIntegerField(verbose_name='Número de Lotes')
    
    prepared_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        related_name='protocols_prepared', 
        verbose_name='Preparado por'
    )
    date_prepared = models.DateField(verbose_name='Fecha de Preparación')
    
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        related_name='protocols_approved', 
        verbose_name='Aprobado por'
    )
    date_approved = models.DateField(verbose_name='Fecha de Aprobación')
    
    enabled_protocol = models.BooleanField(default=True, verbose_name='Protocolo Habilitado')
    version = models.PositiveSmallIntegerField(default=1, verbose_name='Versión')

    class Meta:
        db_table = 'Protocol'
        verbose_name = 'Protocolo'
        verbose_name_plural = 'Protocolos'
        ordering = ['code_protocol', '-version']

    def __str__(self):
        return f"{self.code_protocol} - v{self.version}"
