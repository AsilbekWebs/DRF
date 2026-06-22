from django.urls import path
from .views import *

urlpatterns = [
    path('create_list_product', create_list_product,),
    path('list',list_product),
    path('detail/<int:pk>/',detail_product),
    path('create',create_product),
    path('delete/<int:pk>/', delete_product),
    path('update/<int:pk>/', update_product),
    path('update_partial/<int:pk>/', update_partial_product),
    path('detail_delete_update/<int:pk>/', detail_delete_update),
]