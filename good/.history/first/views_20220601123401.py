from django.shortcuts import render
from .models import *

def home(request):
    if request.method == 'POST':
        
    context = {}
    return render(request, "index.html", context)
