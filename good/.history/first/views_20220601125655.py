from django.shortcuts import render
from .models import *

def home(request):
    if request.method == 'POST' and 'image' in request.FILES:
        first = First()
        name = request.POST['name']
        age = request.POST['age']
        image = request.FILES['image']
        first.save()
    context = {}
    return render(request, "index.html", context)
