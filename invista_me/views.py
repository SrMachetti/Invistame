from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required
'''def pagina_inicial(request):
    return HttpResponse('Proto para investir!')'''

def pagina_contatos(request):
    pessoa = {
        'nome': 'Sergio',
        'idade': 48,
        'hobby': 'cliclismo'
    }
    return render(request, 'investimento/contato.html', pessoa)

def minha_historia(request):
    return render(request, 'investimento/minha_historia.html')

'''def novo_investimento(request):
    return render(request, 'investimento/novo_investimento.html')'''

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request,'investimento/investimento_registrado.html', investimento)

def instetimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimento/investimentos.html', context=dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request,'investimento/detalhe.html', dados)

@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request,'investimento/novo_investimento.html', context=formulario)

@login_required    
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimento/novo_investimento.html',
                      {'formulario':formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')
    
@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimento/confirmar_exclusao.html',{'item': investimento})