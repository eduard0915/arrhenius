from django.urls import path
from core.protocol.views.web_views import (
    ProtocolListView, 
    ProtocolCreateView, 
    ProtocolUpdateView, 
    ProtocolDetailView, 
    ProtocolDeleteView
)

app_name = 'protocol'

urlpatterns = [
    path('list/', ProtocolListView.as_view(), name='protocol_list'),
    path('add/', ProtocolCreateView.as_view(), name='protocol_create'),
    path('update/<uuid:pk>/', ProtocolUpdateView.as_view(), name='protocol_update'),
    path('detail/<uuid:pk>/', ProtocolDetailView.as_view(), name='protocol_detail'),
    path('delete/<uuid:pk>/', ProtocolDeleteView.as_view(), name='protocol_delete'),
]
