from django.shortcuts import render
from .mide


def home(request):

    return render(request, 'index.html')
