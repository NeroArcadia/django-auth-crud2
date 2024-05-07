from django.shortcuts import render
from .models import *


def portafolio(request):
    projects = project.objects.all()
    return render(request, 'portafolio.html', {'projects': projects})
