from .models import Cliente

def get_unknown():
    obj, created = Cliente.objects.get_or_create(nome="Desconhecido")
    return obj
