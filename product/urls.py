from django.urls import path
from product import views

urlpatterns = [
    path('test/', views.test_api_view),
    path('products/', views.product_list_api_view),
    path('products/<int:id>/', views.product_detail_api_view),
]
