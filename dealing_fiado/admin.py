from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Produto)
admin.site.register(models.Venda)
admin.site.register(models.Cliente)
admin.site.register(models.Empregado)
admin.site.register(models.Folha)
admin.site.register(models.Ponto)
