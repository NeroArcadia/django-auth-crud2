from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,'home.html')

def acerca (request):
    return render(request,'acerca.html')

def contacto(request):
    return render(request,'contacto.html')

def pruebas(request):
    return render (request,'pruebas.html')