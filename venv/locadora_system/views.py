from django.shortcuts import render, redirect
from .models import Aluguel
from .form import AluguelForm
import datetime


def home(request):
    data = {}
    data['filmes'] = ['t1', 't2', 't3']

    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now

    return render(request, 'locadora_system/home.html', data)


def listagem(request):
    data = {}
    data['filmes'] = Aluguel.objects.all()
    return render(request, 'locadora_system/listagem.html', data)


def novo_aluguel(request):
    data = {}
    form = AluguelForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'locadora_system/form.html', data)


def update(request, pk):
    data = {}
    filme = Aluguel.objects.get(pk=pk)
    form = AluguelForm(request.POST or None, instance=filme)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['filme'] = filme
    return render(request, 'locadora_system/form.html', data)


def delete(request, pk):
    filme = Aluguel.objects.get(pk=pk)
    filme.delete()
    return redirect('url_listagem')