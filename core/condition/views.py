from core.condition.models import Condition
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from core.mixins import ValidatePermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from core.condition.forms import ConditionForm, ConditionUpdateForm


# Creación de Condición
class ConditionCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Condition
    form_class = ConditionForm
    template_name = 'condition/create_condition.html'
    success_url = reverse_lazy('condition:condition_list')
    permission_required = 'condition.add_condition'
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
                    messages.success(request, f'Condición creada satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Condiciones de Estudios de Estabilidad'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['entity'] = 'Creación de Condiciones de Estudios de Estabilidad'
        context['div'] = '12'
        context['number_column'] = 5
        return context


# Edición de Condición
class ConditionUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Condition
    form_class = ConditionUpdateForm
    template_name = 'condition/create_condition.html'
    success_url = reverse_lazy('condition:condition_list')
    permission_required = 'condition.change_condition'
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
                    messages.success(request, f'Condición editada satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Condiciones de Estudios de Estabilidad'
        context['list_url'] = self.success_url
        context['entity'] = 'Edición de Condiciones de Estudios de Estabilidad'
        context['action'] = 'edit'
        context['div'] = '12'
        context['number_column'] = 5
        return context


# Detalle de Condición
class ConditionDetailView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    model = Condition
    template_name = 'condition/detail_condition.html'
    permission_required = 'condition.view_condition'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(ConditionDetailView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle de Condición'
        context['entity'] = 'Detalle de Condición'
        context['list_url'] = reverse_lazy('condition:condition_list')
        return context


# Listado de Condiciones
class ConditionListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Condition
    template_name = 'condition/list_condition.html'
    permission_required = 'condition.view_condition'

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
                conditions = list(Condition.objects.values(
                    'id',
                    'zone_condition',
                    'description_condition',
                    'study_type',
                    'temperture_inf',
                    'temperture_sup',
                    'percent_humidity_inf',
                    'percent_humidity_sup',
                    'period_minimum_time',
                    'condition_enabled',
                    'version'
                ).order_by('zone_condition', 'study_type', '-version'))
                return JsonResponse(conditions, safe=False)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Condiciones de Estudios de Estabilidad'
        context['create_url'] = reverse_lazy('condition:condition_create')
        context['entity'] = 'Condiciones de Estudios de Estabilidad'
        context['div'] = '12'
        return context
