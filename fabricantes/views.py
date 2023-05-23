from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Fabricante

def fabricantes(request):
    fabricantes = Fabricante.objects.all().values()
    template = loader.get_template('all_fabricantes.html')
    context = {
        'fabricantes': fabricantes,
    }
    return HttpResponse(template.render(context, request))


def detalhes(request, id):
    fabricante = Fabricante.objects.get(id=id)
    template = loader.get_template('detalhes.html')
    context = {
        'fabricante': fabricante,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
