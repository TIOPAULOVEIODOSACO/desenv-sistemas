from django.shortcuts import render

# Create your views here.
from models import Tarefa

from models  import HttpResponse 


def listar_tarefas(request):
    tarefas_salvas = Tarefas.onjects.all()
    contexto = [
                    "minhas_tarefas": tarefas_salvas        
    ]

    return render (request, 'tarefa\lista.html', contexto)