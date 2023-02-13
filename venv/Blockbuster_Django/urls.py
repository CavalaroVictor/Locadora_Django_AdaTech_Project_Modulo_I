from django.contrib import admin
from django.urls import path
from locadora_system.views import home, listagem, novo_aluguel, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listagem, name='url_listagem'),
    path('aluguel/',  novo_aluguel, name='url_aluguel'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('home/',  home)
]