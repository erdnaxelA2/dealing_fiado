from .doing import cliente, empregado, produto, venda

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "dealing_fiado/layout.html")
