from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select
from core.condition.models import Condition
from django.core.exceptions import ValidationError

ZONE = [
    ('Zona I', 'Zona I'), ('Zona II', 'Zona II'), ('Zona III', 'Zona III'), ('Zona IVa', 'Zona IVa'), ('Zona IVb', 'Zona IVb')
]

STUDY_TYPE = [
    ('Acelerado', 'Acelerado'), ('Natural', 'Natural'), ('Intermedio', 'Intermedio')
]

TIME_STUDY = [
    ('3', '3 Meses'), ('6', '6 Meses'), ('12', '12 Meses'), ('24', '24 Meses'), ('36', '36 Meses'), ('60', '60 Meses')
]

class ConditionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

        col_classes = {
            'zone_condition': 'col-md-2',        
            'study_type': 'col-md-2',
            'temperture_sup': 'col-md-2',
            'temperture_inf': 'col-md-2',
            'percent_humidity_sup': 'col-md-2',
            'percent_humidity_inf': 'col-md-2',
            'period_minimum_time': 'col-md-2',
            'detail_condition': 'col-md-6',
            'description_condition': 'col-md-4',         
        }

        for field_name, field in self.fields.items():
            field.col_class = col_classes.get(field_name, 'col-md-3')      

    class Meta:
        model = Condition
        fields = [
            'zone_condition',
            'description_condition',
            'study_type',
            'temperture_inf',
            'temperture_sup',
            'percent_humidity_inf',
            'percent_humidity_sup',
            'period_minimum_time',
            'detail_condition',
        ]
        widgets = {
            'zone_condition': Select(attrs={'class': 'form-control', 'required': True}, choices=ZONE),
            'description_condition': TextInput(attrs={'class': 'form-control', 'required': True}),
            'study_type': Select(attrs={'class': 'form-control', 'required': True}, choices=STUDY_TYPE),
            'temperture_sup': TextInput(attrs={'class': 'form-control', 'required': True}),
            'temperture_inf': TextInput(attrs={'class': 'form-control', 'required': True}),
            'percent_humidity_sup': TextInput(attrs={'class': 'form-control', 'required': True}),
            'percent_humidity_inf': TextInput(attrs={'class': 'form-control', 'required': True}),
            'period_minimum_time': Select(attrs={'class': 'form-control', 'required': True}, choices=TIME_STUDY),
            'detail_condition': TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned = super().clean()
        zone = self.cleaned_data.get('zone_condition')
        # Here we could add validation if needed, similar to ProductForm
        return cleaned


class ConditionUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

        col_classes = {
            'zone_condition': 'col-md-2',        
            'study_type': 'col-md-2',
            'temperture_inf': 'col-md-2',
            'temperture_sup': 'col-md-2',
            'percent_humidity_inf': 'col-md-2',
            'percent_humidity_sup': 'col-md-2',
            'period_minimum_time': 'col-md-2',
            'detail_condition': 'col-md-6',
            'description_condition': 'col-md-4',         
        }

        for field_name, field in self.fields.items():
            field.col_class = col_classes.get(field_name, 'col-md-3')      

    class Meta:
        model = Condition
        fields = [
            'zone_condition',
            'description_condition',
            'study_type',
            'temperture_inf',
            'temperture_sup',
            'percent_humidity_inf',
            'percent_humidity_sup',
            'period_minimum_time',
            'detail_condition',
        ]
        widgets = {
            'zone_condition': Select(attrs={'class': 'form-control', 'required': True}, choices=ZONE),
            'description_condition': TextInput(attrs={'class': 'form-control', 'required': True}),
            'study_type': Select(attrs={'class': 'form-control', 'required': True}, choices=STUDY_TYPE),
            'temperture_sup': TextInput(attrs={'class': 'form-control', 'required': True}),
            'temperture_inf': TextInput(attrs={'class': 'form-control', 'required': True}),
            'percent_humidity_sup': TextInput(attrs={'class': 'form-control', 'required': True}),
            'percent_humidity_inf': TextInput(attrs={'class': 'form-control', 'required': True}),
            'period_minimum_time': Select(attrs={'class': 'form-control', 'required': True}, choices=TIME_STUDY),
            'detail_condition': TextInput(attrs={'class': 'form-control'}),
        }
