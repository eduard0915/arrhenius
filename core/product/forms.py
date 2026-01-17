from django.forms import ModelForm
from core.product.models import Product
from django.forms import Select, TextInput
from django.core.exceptions import ValidationError


TYPE_PROD = [
    ('Cosmetico', 'Cosmetico'),
    ('Medicamento', 'Medicamento') 
]

FORM_PHARMACEUTICAL = [
    ('Tableta', 'Tableta'),
    ('Solución', 'Solución'),
    ('Suspensión', 'Suspensión'),
    ('Emulsión', 'Emulsión'),
    ('Inyección', 'Inyección'),
    ('Jarabe', 'Jarabe'),
    ('Gotas', 'Gotas'),
    ('Crema', 'Crema'),
    (' Gel', ' Gel'),
    (' Gel', ' Gel'),
]


# Creación de producto
class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

            col_classes = {
            'type_prod': 'col-md-2',     
            'code_product': 'col-md-3',
            'description_product': 'col-md-5',
            'pharma_form': 'col-md-2',
            'brand_product': 'col-md-2',
            'sanitary_license': 'col-md-2',
            'image_product': 'col-md-2',
        }

        for field_name, field in self.fields.items():
            field.col_class = col_classes.get(field_name, 'col-md-3')

    class Meta:
        model = Product
        fields = [
            'type_prod',
            'code_product',
            'description_product',
            'pharma_form',
            'brand_product',
            'sanitary_license',
            'image_product'
        ]

        widgets = {
            'type_prod': Select(attrs={'class': 'form-control', 'required': True}, choices=TYPE_PROD),            
            'code_product': TextInput(attrs={'class': 'form-control', 'required': True}),
            'description_product': TextInput(attrs={'class': 'form-control', 'required': True}),
            'pharma_form': Select(attrs={'class': 'form-control'}, choices=FORM_PHARMACEUTICAL),
            'brand_product': TextInput(attrs={'class': 'form-control'}),
            'sanitary_license': TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned = super().clean()
        code = self.cleaned_data.get('code_product')
        if Product.objects.filter(code_product=code, version=1).exists():
            raise ValidationError('El código registrado ya está asignado a otro producto!')
        return cleaned


# Edición de producto
class ProductUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Product
        fields = [
            'type_prod',
            'code_product',
            'description_product',
            'pharma_form',
            'brand_product',
            'sanitary_license',
            'image_product'
        ]
        widgets = {
            'type_prod': Select(attrs={'class': 'form-control', 'required': True}, choices=TYPE_PROD),            
            'code_product': TextInput(attrs={'class': 'form-control', 'required': True}),
            'description_product': TextInput(attrs={'class': 'form-control', 'required': True}),
            'pharma_form': Select(attrs={'class': 'form-control'}, choices=FORM_PHARMACEUTICAL),
            'brand_product': TextInput(attrs={'class': 'form-control'}),
            'sanitary_license': TextInput(attrs={'class': 'form-control'})
        }


