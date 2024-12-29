from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListCreate.as_view(), name='product_list_create'),
    path('<int:product_id>/', views.ProductDetail.as_view(), name='product_detail'),
]