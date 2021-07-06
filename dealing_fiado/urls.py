from django.urls import path, include

from . import views

cliente = [
    path("", views.cliente.ClienteListView.as_view(), name="list_cliente"),
    path("gerar", views.cliente.ClienteCreateView.as_view(), name="form_cliente"),
    path("<int:pk>/", views.cliente.ClienteDetailView.as_view(), name="detail_cliente"),
    path("<int:pk>/atualizar", views.cliente.ClienteUpdateView.as_view(), name="update_cliente"),
    path("<int:pk>/deletar", views.cliente.ClienteDeleteView.as_view(), name="delete_cliente"),
]

produto = [
    path("", views.produto.ProdutoListView.as_view(), name="list_produto"),
    path("gerar", views.produto.ProdutoCreateView.as_view(), name="form_produto"),
    path("<int:pk>/", views.produto.ProdutoDetailView.as_view(), name="detail_produto"),
    path("<int:pk>/atualizar", views.produto.ProdutoUpdateView.as_view(), name="update_produto"),
    path("<int:pk>/deletar", views.produto.ProdutoDeleteView.as_view(), name="delete_produto"),
]

venda = [
    path("", views.venda.VendaListView.as_view(), name="list_venda"),
    path("gerar", views.venda.VendaCreateView.as_view(), name="form_venda"),
    path("<int:pk>/", views.venda.VendaDetailView.as_view(), name="detail_venda"),
    path("<int:pk>/atualizar", views.venda.VendaCreateView.as_view(), name="update_venda"),
    path("<int:pk>/deletar", views.venda.VendaDeleteView.as_view(), name="delete_venda")
]

folha = [
    path("", views.empregado.FolhaListView.as_view(), name="list_folha"),
    path("gerar", views.empregado.FolhaCreateView.as_view(), name="form_folha"),
    path("<int:pk>/", views.empregado.FolhaDetailView.as_view(), name="detail_folha"),
    path("<int:pk>/atualizar", views.empregado.FolhaUpdateView.as_view(), name="update_folha"),
    path("<int:pk>/deletar", views.empregado.FolhaDeleteView.as_view(), name="delete_folha"),

    path("<int:pk_folha>/pontos/<str:view>", views.empregado.PontosDealing.as_view(), name="folha_pontos"),
]

empregado = [
    path("", views.empregado.EmpregadoListView.as_view(), name="list_empregado"),
    path("gerar", views.empregado.EmpregadoCreateView.as_view(), name="form_empregado"),
    path("folha/", include(folha)),
    path("<int:pk>/", views.empregado.EmpregadoDetailView.as_view(), name="detail_empregado"),
    path("<int:pk>/atualizar", views.empregado.EmpregadoUpdateView.as_view(), name="update_empregado"),
    path("<int:pk>/deletar", views.empregado.EmpregadoDeleteView.as_view(), name="delete_empregado"),
]

urlpatterns = [
    path("", views.index, name="index"),
    path("cliente/", include(cliente)),
    path("produto/", include(produto)),
    path("venda/", include(venda)),
    path("empregado/", include(empregado)),
]
