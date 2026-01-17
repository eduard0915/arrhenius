from core.product.models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from core.mixins import ValidatePermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from core.product.forms import ProductForm, ProductUpdateForm


# Creación de producto
class ProductCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create_product.html'
    success_url = reverse_lazy('product:product_list')
    permission_required = 'products.add_product'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                    messages.success(request, f'Producto creado satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Producto'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['entity'] = 'Creación de Producto'
        context['div'] = '12'
        context['number_column'] = 4
        return context


# Edición de Producto
class ProductUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'product/create_product.html'
    success_url = reverse_lazy('product:product_list')
    permission_required = 'products.change_product'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                    messages.success(request, f'Producto editado satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Producto'
        context['list_url'] = self.success_url
        context['entity'] = 'Edición de Producto'
        context['action'] = 'edit'
        context['div'] = '12'
        context['number_column'] = 4
        return context
    

# Detalle de Producto
class ProductDetailView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'product/detail_product.html'
    permission_required = 'products.view_product'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(ProductDetailView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle de Producto'
        context['entity'] = 'Detalle de Producto'
        context['list_url'] = reverse_lazy('product:product_list')
        return context


# Listado de productos
class ProductListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Product
    template_name = 'product/list_product.html'
    permission_required = 'products.view_product'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                material = list(Product.objects.values(
                    'id',
                    'code_product',
                    'description_product',
                    'pharma_form',
                    'product_enabled',
                    'brand_product',
                    'sanitary_license',
                    'type_prod',                
                    'version'
                ).order_by('-code_product', '-version'))
                return JsonResponse(material, safe=False)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        context['title'] = 'Productos'      
        context['create_url'] = reverse_lazy('product:product_create')    
        context['entity'] = 'Productos'
        context['div'] = '12'
        return context
    