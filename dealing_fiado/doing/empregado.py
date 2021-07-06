from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

import re

from ..forms import PontoForm
from ..models import Empregado, Folha, Ponto

# Empregado
class EmpregadoListView(ListView):
    model = Empregado
    context_object_name = "empregados"
    ordering = ["-nome"]

class EmpregadoDetailView(DetailView):
    model = Empregado
    context_object_name = "empregado"

class EmpregadoCreateView(CreateView):
    model = Empregado
    fields = "__all__"

    def form_valid(self, form):
        return super().form_valid(form)

class EmpregadoUpdateView(UpdateView):
    model = Empregado
    fields = "__all__"

    def form_valid(self, form):
        return super().form_valid(form)

class EmpregadoDeleteView(DeleteView):
    model = Empregado
    context_object_name = 'empregado'
    success_url = '/'

# Folha
class FolhaListView(ListView):
    model = Folha
    context_object_name = "folhas"
    ordering = ["-data_inicial"]

class FolhaDetailView(DetailView):
    model = Folha
    context_object_name = "folha"

class FolhaCreateView(CreateView):
    model = Folha
    fields = "__all__"

    def form_valid(self, form):
        return super().form_valid(form)

class FolhaUpdateView(UpdateView):
    model = Folha
    fields = "__all__"

    def form_valid(self, form):
        return super().form_valid(form)

class FolhaDeleteView(DeleteView):
    model = Folha
    context_object_name = "folha"
    success_url = '/'

# Ponto
class PontosDealing(View):

    folha = get_object_or_404(Folha, pk=pk)

    def get(self, request, pk, view=None):
        if view is None:
            context = {
                "form": PontoForm()
            }
            return render(request, "dealing_fiado/ponto_form.html", context)
        match = re.match(r"/(?P<pk>\d+)/?(?P<action>\w+)?", view)
        if match:
            g = match.groupdict()
            ponto = get_object_or_404(Ponto, pk=g["pk"])
            

    def post(self, request, pk):
        pass
