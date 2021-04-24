from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('supermercado.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]
