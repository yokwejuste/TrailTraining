from django.shortcuts import render
from .models import *


def home(request):
    if request.method == "POST":
        name = method
    return render(request, 'index.html')
