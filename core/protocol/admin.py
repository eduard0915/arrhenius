from django.contrib import admin
from core.protocol.models import Protocol


@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = (
        'code_protocol', 
        'study_type', 
        'condition', 
        'prepared_by', 
        'date_prepared', 
        'approved_by', 
        'date_approved', 
        'enabled_protocol', 
        'version'
    )
    list_filter = ('enabled_protocol', 'study_type', 'condition', 'version')
    search_fields = ('code_protocol', 'study_type', 'objective')
    readonly_fields = ('id', 'date_creation', 'date_updated')
    ordering = ('code_protocol', '-version')
    list_per_page = 25
