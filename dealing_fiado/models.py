from django.db import models
from django.utils import timezone
from django.urls import reverse

from datetime import datetime, timedelta

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=20)
    valor = models.DecimalField(decimal_places=2, max_digits=100)

    def get_absolute_url(self):
        return reverse("detail_produto", kwargs={"pk": self.pk})

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    compras_fiados = models.ManyToManyField("Venda", blank=True, related_name="cliente_compras_fiados")

    def get_absolute_url(self):
        return reverse("detail_cliente", kwargs={"pk": self.pk})

    def __str__(self):
        return self.nome

class Venda(models.Model):
    data_inicial = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mercadorias = models.ManyToManyField(Produto, blank=True)
    produtos = models.TextField(blank=True)
    # produtos = models.JSONField(blank=True)
    valor = models.DecimalField(decimal_places=2, max_digits=100, blank=True)
    pago = models.BooleanField(default=False)
    data_final = models.DateTimeField(blank=True)

    def save(self, *args, **kargs):
        if not self.id:
            self.data_inicial = timezone.now()
        if not self.pago:
            if not self.data_final:
                self.data_final = self.data_inicial + timedelta(days=30)
        else:
            self.data_final = self.data_inicial
        super(Venda, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("detail_venda", kwargs={"pk": self.pk})
        #return reverse("list_venda")

    def __str__(self):
        return f"Cliente: {self.cliente.nome} - Pago: {self.pago}"

class Ponto(models.Model):
    entrada = models.DateTimeField(blank=True)
    intervalo = models.DateTimeField(blank=True)
    retorno = models.DateTimeField(blank=True)
    saida = models.DateTimeField(blank=True)

class Folha(models.Model):
    empregado = models.ForeignKey("Empregado", on_delete=models.CASCADE)
    data_inicial = models.DateTimeField(blank=True)
    pontos = models.ManyToManyField(Ponto, blank=True)
    data_final = models.DateTimeField(blank=True)

class Empregado(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    folhas = models.ManyToManyField(Folha, blank=True, related_name="empregado_folhas")

    def get_absolute_url(self):
        return reverse("detail_empregado", kwargs={"pk": self.pk})

    def __str__(self):
        return self.nome
