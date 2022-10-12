from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',context={'text':'Hello World'})

def lobby(request):
    return render(request,'lobby.html')

def graph(request):
    return render(request,'base.html',context={'text':'Hello World'})