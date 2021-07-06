from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from ..models import Produto

# Produto
class ProdutoListView(ListView):
    model = Produto
    context_object_name = "produtos"
    ordering = ["-nome"]

class ProdutoDetailView(DetailView):
    model = Produto
    context_object_name = "produto"

class ProdutoCreateView(CreateView):
    model = Produto
    fields = "__all__"

    def form_valid(self, form):
        return super().form_valid(form)

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = "__all__"

    def form_valid(self, form):
        return super().form_valid(form)

class ProdutoDeleteView(DeleteView):
    model = Produto
    context_object_name = 'produto'
    success_url = '/'
