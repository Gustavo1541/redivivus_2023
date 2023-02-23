from django.urls import path    # funções para criar os caminhos dentro de auth/
from . import views             # da pasta que eu estou, importe o arquivo views.py

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.logar, name="login"),
    path('sair/', views.sair, name="sair"),

]