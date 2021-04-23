from django.urls import path
from .views import super_index

urlpatterns =[
    path('', super_index, name='super_index'),
]