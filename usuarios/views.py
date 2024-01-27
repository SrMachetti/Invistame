'''
1. Criar nova rota url.py
2. Criar função responsável por entregar esta rota
3. Criar um template para exibir os dados e 
'''
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout

def novo_usuario(request):
    #tipo de requisição, Validar, Informar, Salvar
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)  #populando a classe com o que foi enviado
        if formulario.is_valid():
            # salvar
            formulario.save()
            #informar
            usuario = formulario.cleaned_data.get('username')
            messages.success(request,f'o usuário {usuario} foi criado com sucesso!')
            return redirect('investimentos')
            '''
            outros tipos de mensagens
            messages.debug
            messages.info
            messages.success
            messages.warning
            messages.error
            '''
        else:
            messages.warning(request,f'ouve um erro')
    else:
        formulario = UserRegisterForm()
    return render(request, 'usuarios/registrar.html', {'formulario':formulario})

def logout_view(request):
    logout(request)
    return render(request,'usuarios/logout.html')
 
