from django.shortcuts import render
from .models import *


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
    return render(request, 'index.html')
