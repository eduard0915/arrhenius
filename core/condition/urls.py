from django.urls import path
from core.condition.views import *

app_name = 'condition'

urlpatterns = [
    path('add/', ConditionCreateView.as_view(), name='condition_create'),
    path('list/', ConditionListView.as_view(), name='condition_list'),
    path('update/<uuid:pk>/', ConditionUpdateView.as_view(), name='condition_update'),
    path('detail/<uuid:pk>/', ConditionDetailView.as_view(), name='condition_detail'),
]
