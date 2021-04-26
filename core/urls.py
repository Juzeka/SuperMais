from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('supermercado.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('pedido/', include('pedido.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/usuario/', include('dashboarduser.urls')),
    path('account/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
