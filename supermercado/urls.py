from django.urls import path
from .views import home_super

urlpatterns =[
    path('', home_super, name='super_home'),
]