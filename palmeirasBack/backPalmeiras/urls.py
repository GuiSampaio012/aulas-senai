from django.urls import path
from rest_framework import routers
from. import views

# router = routers.SimpleRouter()
# router.register('clientes',views.ClienteViewSet)

urlpatterns = [
    # path('clientes', view=views.ListarClientes.as_view()),
    # path('clientes/<int:pk>', view=views.DetalharClientes.as_view()),
    path('categorias', view=views.Categoria.as_view()),
    path('categorias/<int:pk>', view=views.CategoriaDetalhe.as_view()),
    path('produtos', view=views.ProdutoList.as_view()),
    path('produtos/<int:pk>', view=views.ProdutoDetalhe.as_view()),   
]
# +router.urls