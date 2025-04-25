from django.urls import path
from . import views

urlpatterns = [
    path('',views.feriado),
    path('listar_feriados/',views.listar_feriados, name='listar_feriados'),
    path('adicionar/', views.adicionar_feriado, name='adicionar_feriado'),
    path('remover/<int:id>/', views.remover_feriado, name='remover_feriado'),
    path('atualizar/<int:id>/', views.atualizar_feriado, name='atualizar_feriado')
]
