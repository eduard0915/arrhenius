from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from core.mixins import ValidatePermissionRequiredMixin
from core.protocol.models import Protocol
from core.protocol.forms import ProtocolForm
from core.protocol.selectors.protocol_selectors import protocol_list_selector, protocol_detail_selector
from core.protocol.services.protocol_services import protocol_create_service, protocol_update_service, protocol_delete_service


class ProtocolListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Protocol
    template_name = 'protocol/list_protocol.html'
    permission_required = 'protocol.view_protocol'

    def get_queryset(self):
        return protocol_list_selector()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for p in self.get_queryset():
                    data.append({
                        'id': p.id,
                        'code_protocol': p.code_protocol,
                        'study_type': p.study_type,
                        'condition': p.condition.zone_condition,
                        'prepared_by': p.prepared_by.get_full_name(),
                        'date_prepared': p.date_prepared.strftime('%Y-%m-%d'),
                        'enabled_protocol': p.enabled_protocol,
                        'version': p.version,
                    })
                return JsonResponse(data, safe=False)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Protocolos'
        context['create_url'] = reverse_lazy('protocol:protocol_create')
        context['entity'] = 'Listado de Protocolos'
        context['div'] = '12'
        return context


class ProtocolCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Protocol
    form_class = ProtocolForm
    template_name = 'protocol/create_protocol.html'
    success_url = reverse_lazy('protocol:protocol_list')
    permission_required = 'protocol.add_protocol'

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
                    # Using service for creation
                    protocol_create_service(**form.cleaned_data)
                    messages.success(request, 'Protocolo creado satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Protocolo'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['entity'] = 'Creación de Protocolo'
        context['div'] = '12'
        return context


class ProtocolUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Protocol
    form_class = ProtocolForm
    template_name = 'protocol/create_protocol.html'
    success_url = reverse_lazy('protocol:protocol_list')
    permission_required = 'protocol.change_protocol'

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
                    # Using service for update
                    protocol_update_service(self.object, **form.cleaned_data)
                    messages.success(request, 'Protocolo editado satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Protocolo'
        context['list_url'] = self.success_url
        context['entity'] = 'Edición de Protocolo'
        context['action'] = 'edit'
        context['div'] = '12'
        return context


class ProtocolDetailView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    model = Protocol
    template_name = 'protocol/detail_protocol.html'
    permission_required = 'protocol.view_protocol'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle del Protocolo'
        context['entity'] = 'Detalle del Protocolo'
        context['list_url'] = reverse_lazy('protocol:protocol_list')
        return context


class ProtocolDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Protocol
    success_url = reverse_lazy('protocol:protocol_list')
    permission_required = 'protocol.delete_protocol'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object = self.get_object()
            protocol_delete_service(self.object)
            messages.success(request, 'Protocolo eliminado satisfactoriamente!')
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
