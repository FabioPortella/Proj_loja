from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Fabricante
from tipo.models import Tipos

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


def add(request):
    tipos = Tipos.objects.all().values()
    template = loader.get_template('add.html')
    context = {
        'tipos': tipos,
    }
    return HttpResponse(template.render(context, request))

def addrecord(request):
    nome = request.POST['nome']
    endereco = request.POST['endereco']
    telefone = request.POST['telefone']
    email = request.POST['email']
    tipo = Tipos.objects.filter(id=request.POST['tipo']).first()
    
    fabricante = Fabricante(
        nome=nome, 
        endereco=endereco, 
        telefone=telefone, 
        email=email,
        tipo = tipo)
    fabricante.save()
    return HttpResponseRedirect(reverse('fabricantes'))

def delete(request, id):
    fabricante = Fabricante.objects.get(id=id)
    fabricante.delete()
    return HttpResponseRedirect(reverse('fabricantes'))

def update(request, id):
    fabricante = Fabricante.objects.get(id=id)
    tipos = Tipos.objects.all().values()
    template = loader.get_template('update.html')
    context = {
        'fabricante': fabricante,
        'tipos': tipos,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    nome = request.POST['nome']
    endereco = request.POST['endereco']
    telefone = request.POST['telefone']
    email = request.POST['email']
    tipo = request.POST['tipo']

    fabricante = Fabricante.objects.get(id=id)
    fabricante.nome = nome
    fabricante.endereco = endereco
    fabricante.telefone = telefone
    fabricante.email = email
    fabricante.tipo = Tipos.objects.get(id=tipo)
    
    fabricante.save()
    return HttpResponseRedirect(reverse('fabricantes')) 