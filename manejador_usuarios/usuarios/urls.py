from django.urls import path
from . import views

urlpatterns = [
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('formulario_usuario/', views.formulario_usuario, name='formulario_usuario'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('listar_usuarios/<int:usuario_id>/', views.listar_usuarios, name='listar_usuario_por_id'),
    path('', views.pagina_principal_usuarios, name='pagina_principal_usuarios'),

]