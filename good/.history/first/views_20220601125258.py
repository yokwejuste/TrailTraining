from django.shortcuts import render
from .models import *

def home(request):
    if request.method == 'POST' and request.FILES['image']:
        first = First()
        first.name = request.POST['name']
        first.age = request.POST['age']
        first.image = request.FILES['image']
        first.save()
    context = {}
    return render(request, "index.html", context)
