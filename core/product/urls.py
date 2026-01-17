from django.conf.urls.static import static
from django.urls import path

from studystb import settings
from core.product.views import *

app_name = 'product'

urlpatterns = [
    path('add/', ProductCreateView.as_view(), name='product_create'), 
    path('list/', ProductListView.as_view(), name='product_list'),    
    path('update/<uuid:pk>/', ProductUpdateView.as_view(), name='product_update'),    
    path('detail/<uuid:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
