from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_products, name='all_products'),
    path('<int:product_id>/', views.get_product_by_id, name='get_product_by_id'),
    path('in-stock/', views.get_products_in_stock, name='get_products_in_stock'),
    path('discounted/', views.get_products_on_discount, name='get_products_on_discount'),
    path('categories/', views.get_all_categories, name='get_all_categories'),
    path('search/<str:search_query>/', views.search_products_by_title, name='search_products_by_title'),
]
