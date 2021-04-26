from django.urls import path
from .views import login,novo_usuario,logout

urlpatterns =[
    path('login/', login, name='login'),
    path('novo/', novo_usuario, name='novo_usuario'),
    path('logout/', logout, name='logout'),
]