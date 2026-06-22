from django.urls import path
from .views import *

urlpatterns = [
    path('list/', list_tests),
    path('detail/<int:pk>/', detail_tests),
    path('update/<int:pk>/', update_tests),
    path('create', create_tests),
    path('delete/<int:pk>/', delete_tests),
]