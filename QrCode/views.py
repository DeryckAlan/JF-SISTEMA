from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from Projeto.models import Projeto, Painel
from .models import QRcode
from .forms import QRcodeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

# Create your views here.
def QRcodeList(request):
    qrcodeList = QRcode.objects.all()
    projectList = Projeto.objects.all()
    painelList = Painel.objects.all()
    return render(request, 'qrcode_list.html', {'qrcodelist': qrcodeList, 'projectlist': projectList, 'painellist': painelList})

def QRcodeCreate(request):
    
    form = QRcodeForm(request.POST or None)

    if request.method=="GET":
        return render(request, 'modal_createqrcode.html', {'QRcodeForm': form})

    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('/qrlist')
        
    return render(request, 'modal_createqrcode.html', {'QRcodeForm':form})

def QRcodeUpdate(request, pk):
    item = QRcode.objects.get(pk=pk)
    form = QRcodeForm(request.POST or None, instance=item)
    
    if request.method=="GET":
        context = {
            'QRcodeForm': form,
            'item': item
        }
        
        return render(request, 'model_updateqrcode.html', context)
        
    elif request.method=="POST":
        if form.is_valid():
            form.save()
            
            return redirect('/qrlist')
            
    context = {
        'item': item,
    }
    
    return HttpResponse(template.render(context, request))

def QRcodeDelete(request, id):
    item = QRcode.objects.get(id=id)
    item.delete()
    return redirect('/qrlist')