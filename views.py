#from _typeshed import WriteableBuffer
#from calc.forms import WriterForm
from typing import ContextManager
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import WriterForm
from .models import Writer
# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def index(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'writer_page.html',{'username':username})
        else:
            messages.info(request,'invalid credentials')
            return HttpResponseRedirect('index')
    else:
        return render(request,'index.html')

def writer_page(request):
    return render(request,'writer_page.html')

def logout(request):
    auth.logout(request)
    return render(request,'welcome.html')

def writer_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form=WriterForm()
        else:
            writer=Writer.objects.get(pk=id)
            form=WriterForm(instance=writer)
        return render(request,'writer_form.html',{'form':form})
    else:
        if id==0:
            form=WriterForm(request.POST)
        else:
            writer=Writer.objects.get(pk=id)
            form=WriterForm(request.POST,instance=writer)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('writer_list')

def writer_delete(request,id):
    writer=Writer.objects.get(pk=id)
    writer.delete()
    return render(request,'writer_list.html')

def writer_list(request):
    context = {'writer_list':Writer.objects.all()}
    return render(request,'writer_list.html',context)

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,"result.html",{'result':res})
