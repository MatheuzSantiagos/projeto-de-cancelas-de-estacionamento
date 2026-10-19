from django.shortcuts import render


from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

def pagina_inicial(request):
    return render(request, 'Estacionamento/pagina_inicial.html')
# Create your views here.
