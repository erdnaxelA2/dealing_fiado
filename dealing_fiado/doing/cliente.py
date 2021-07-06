from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from ..models import Cliente

# Cliente
class ClienteListView(ListView):
    model = Cliente
    context_object_name = "clientes"
    ordering = ["-nome"]

class ClienteDetailView(DetailView):
    model = Cliente
    context_object_name = "cliente"

class ClienteCreateView(CreateView):
    model = Cliente
    fields = "__all__"

    def form_valid(self, form):
        return super().form_valid(form)

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = "__all__"

    def form_valid(self, form):
        return super().form_valid(form)

class ClienteDeleteView(DeleteView):
    model = Cliente
    context_object_name = "cliente"
    success_url = '/'
