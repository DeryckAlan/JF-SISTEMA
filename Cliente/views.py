from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente

def clientes(request):

    return render(request, 'clientes.html')
