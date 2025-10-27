from django.urls import path
from . import views 
urlpatterns = [

    path('',views.listar_tarefas, name ='lista_tarefas'),
    #DETALHES DA TAREFA
    #<int:tarefa_id>- captura um numero da URL
    path('<int:tarefa_id>/', views.detalhe_tarefa, name='detalhe_tarefa'),

    path ('adicionar/', views.adicionar_tarefa, name = 'adicionar_tarefa')
]
