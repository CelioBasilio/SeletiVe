from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.messages import constants
from django.contrib import messages
from empresa.models import Vagas

# Create your views here.

def nova_vaga(request):
    # coleta os dados do html
    if request.method == "POST":
       # nome da variavel = metudo para coleta ('nome no html')
        titulo = request.POST.get('titulo')
        email = request.POST.get('email')
        tecnologias_domina = request.POST.getlist('tecnologias_domina') # getlist = seleciona lista | get = seleciona itenm
        tecnologias_nao_domina = request.POST.getlist('tecnologias_nao_domina')
        experiencia = request.POST.get('experiencia')
        data_final = request.POST.get('data_final')
        empresa = request.POST.get('empresa')
        status = request.POST.get('status')

        # passa os dados para a tabela

        vaga = Vagas(
                  # tabela do Banco = variavel criada acima 
                    titulo = titulo,
                    email = email,
                    nivel_experiencia = experiencia,
                    data_final = data_final,
                    empresa_id = empresa,
                    status = status,
        )

        # salva na tabela do banco
        vaga.save()

        # adiciona as tecnologias  * = descompacta a lista 
        vaga.tecnologias_estudar.add(*tecnologias_nao_domina)
        vaga.tecnologias_dominadas.add(*tecnologias_domina)

        # salva no banco
        vaga.save()

        # coleta a mensagem para exibir na proxima url
        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        return redirect(f'/home/empresa/{empresa}')

    # gera um erro de pagina não encontrada. 
    elif request.method == "GET":
        raise Http404()


