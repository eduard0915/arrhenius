from django import forms
from core.protocol.models import Protocol


class ProtocolForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = [
            'code_protocol', 
            'study_type', 
            'condition', 
            'objective', 
            'numbers_batch', 
            'prepared_by', 
            'date_prepared', 
            'approved_by', 
            'date_approved', 
            'enabled_protocol', 
            'version'
        ]
        widgets = {
            'code_protocol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código'}),
            'study_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el tipo de estudio'}),
            'condition': forms.Select(attrs={'class': 'form-control select2'}),
            'objective': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese el objetivo'}),
            'numbers_batch': forms.NumberInput(attrs={'class': 'form-control'}),
            'prepared_by': forms.Select(attrs={'class': 'form-control select2'}),
            'date_prepared': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'approved_by': forms.Select(attrs={'class': 'form-control select2'}),
            'date_approved': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'enabled_protocol': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'version': forms.NumberInput(attrs={'class': 'form-control'}),
        }
