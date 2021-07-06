import time
import json

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView
)

from ..models import Venda, Produto
from ..forms import VendaForms

# Venda
class VendaListView(ListView):
    model = Venda
    context_object_name = "vendas"
    ordering = ["-data_inicial"]

class VendaDetailView(DetailView):
    model = Venda
    context_object_name = "venda"

class VendaCreateView(View):
    # x = re.compile("\[(\d+):(\d+)\]")

    def get(self, request, pk=None):
        if pk is None:
            form = VendaForms()
        else:
            venda = Venda.objects.get(pk=pk)
            form = VendaForms(initial={
                "cliente": venda.cliente, 
                "produtos": [i.pk for i in venda.mercadorias.all()],
                "quantidades": venda.produtos,
                "valor": venda.valor,
                "pago": venda.pago,
                "data_final": venda.data_final
            })

        context = {
            "form": form
        }

        return render(request, "dealing_fiado/venda_form.html", context)

    def post(self, request, pk=None):
        form = VendaForms(request.POST)

        if form.is_valid():
            #{'cliente': <Cliente: Alexandre>, 'produtos': <QuerySet [<Produto: cc 1L>]>, 'valor': None, 'pago': True}
            try:
                quantidades = [int(valor) for valor in form.cleaned_data["quantidades"].split('-')]
                produtos = [produto.pk for produto in form.cleaned_data["produtos"]]
            except ValueError:
                quantidades = None
                produtos = None

            try:
                t1 = time.perf_counter()

                cliente = form.cleaned_data["cliente"]
                valor = form.cleaned_data["valor"]
                pago = form.cleaned_data["pago"]
                data_final = form.cleaned_data["data_final"]

                valor_final = 0
                changed = []

                while 1:

                    if produtos is not None and quantidades is not None:

                        if len(produtos) != len(quantidades):
                            form.add_error(None, "Você deve informar algum produto, ou valor final.")
                            form.add_error("produtos", "Os produtos selecionados devem ser associados respectivamente com alguma quantidade")
                            form.add_error("quantidades", "Você deve informar as qunatidades respectivas aos produtos da vanda, separados por '-', ex: 1-4-6 ")
                            break

                    if pk is None:
                        venda = Venda(cliente=cliente, pago=pago, data_final=data_final)
                        changed.append(0)
                    else:
                        venda = Venda.objects.get(pk=pk)

                        if venda.cliente != cliente:
                            venda.cliente.compras_fiados.remove(venda)
                            venda.cliente = cliente
                            changed.append("cliente")

                        if valor is not None and venda.valor != valor:
                            venda.valor = valor
                            changed.append("valor")

                        if pago is not None and venda.pago != pago:
                            venda.pago = pago
                            changed.append("pago")

                        if data_final is not None and venda.data_final != data_final:
                            venda.data_final = data_final
                            changed.append("data_final")
                        elif venda.data_final == data_final or data_final is None:
                            venda.data_final = None
                            changed.append("data_final")
                        else:
                            pass

                    if quantidades is not None and produtos is not None:
                        for i in zip(produtos, quantidades):
                            valor_final += i[1]*Produto.objects.get(pk=i[0]).valor
                        venda.produtos = '-'.join([str(i) for i in quantidades])
                        venda.valor = valor_final
                        changed.append("produtos")
                        changed.append("valor")

                    if 0 in changed:
                        venda.save()
                    elif len(changed) > 0:
                        print(changed)
                        venda.save(update_fields=set(changed))
                    else:
                        form.add_error(None, "Nenhuma alteração detectada, ação interrompida")
                        break

                    venda.mercadorias.clear()
                    for produto in produtos:
                        venda.mercadorias.add(produto)
                    venda.cliente.compras_fiados.add(venda)

                    t2 = time.perf_counter()

                    print(f"{t2-t1}")

                    print(venda.cliente, venda.produtos, venda.valor)

                    return redirect(venda.get_absolute_url())

            except Exception as e:
                form.add_error(None, f"Algo deu errado, verifique as informações fornecidas. Error: str_{e.__str__()} / repr_{e.__repr__()} .")

        context = {
            "form": form
        }

        return render(request, "dealing_fiado/venda_form.html", context)

class VendaDeleteView(DeleteView):
    model = Venda
    context_object_name = 'venda'
    success_url = '/'
