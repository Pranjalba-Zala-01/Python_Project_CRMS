from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import CriminalForm, VictimForm, WriterForm
from .models import Criminal, Victim, Writer

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'writer_page.html',{'username':username})
        else:
            messages.info(request,'invalid credentials please try again')
            return redirect('login')
    else:
        return render(request,'login.html')

def writer_page(request):
    return render(request,'writer_page.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

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
        return redirect('writer_list')

def criminal_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form=CriminalForm()
        else:
            criminal=Criminal.objects.get(pk=id)
            form=CriminalForm(instance=criminal)
        return render(request,'criminal_form.html',{'form':form})
    else:
        if id==0:
            form=CriminalForm(request.POST)
        else:
            criminal=Criminal.objects.get(pk=id)
            form=CriminalForm(request.POST,instance=criminal)
        if form.is_valid():
            form.save()
        return redirect('criminal_list')

def victim_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form=VictimForm()
        else:
            victim=Victim.objects.get(pk=id)
            form=VictimForm(instance=victim)
        return render(request,'victim_form.html',{'form':form})
    else:
        if id==0:
            form=VictimForm(request.POST)
        else:
            victim=Victim.objects.get(pk=id)
            form=VictimForm(request.POST,instance=victim)
        if form.is_valid():
            form.save()
        return redirect('victim_list')

def writer_delete(request,id):
    writer=Writer.objects.get(pk=id)
    writer.delete()
    return redirect('writer_list')

def criminal_delete(request,id):
    criminal=Criminal.objects.get(pk=id)
    criminal.delete()
    return redirect('criminal_list')

def victim_delete(request,id):
    victim=Victim.objects.get(pk=id)
    victim.delete()
    return redirect('victim_list')

def writer_list(request):
    context = {'writer_list':Writer.objects.all()}
    return render(request,'writer_list.html',context)

def criminal_list(request):
    context = {'criminal_list':Criminal.objects.all()}
    return render(request,'criminal_list.html',context)

def victim_list(request):
    context = {'victim_list':Victim.objects.all()}
    return render(request,'victim_list.html',context)

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,"result.html",{'result':res})