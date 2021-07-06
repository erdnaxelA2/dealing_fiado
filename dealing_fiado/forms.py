from django import forms

from .models import Produto, Cliente, Ponto

class VendaForms(forms.Form):
    cliente = forms.ModelChoiceField(Cliente.objects.all(), required=True)
    produtos = forms.ModelMultipleChoiceField(Produto.objects.all(), required=False)
    #categories.widget.attrs.update({})
    quantidades = forms.CharField(
        required=False,
        widget=forms.TextInput()
    )
    valor = forms.DecimalField(
        decimal_places=2, 
        max_digits=100, 
        required=False,
        widget=forms.TextInput()
    )
    pago = forms.BooleanField(
        required=False,
    )
    data_final = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "dd/mm/aaaa --:--"})
    )

class PontoForm(forms.Form):
    entrada = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(attrs={"type": "datetime-local"})
    )
    intervalo = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(attrs={"type": "datetime-local"})
    )
    retorno = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(attrs={"type": "datetime-local"})
    )
    saida = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(attrs={"type": "datetime-local"})
    )
