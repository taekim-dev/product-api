from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_products, name='all_products'),
    path('<int:product_id>/', views.get_product_by_id, name='get_product_by_id'),
]
