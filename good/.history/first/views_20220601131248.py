from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def home(request):
    if request.method == 'POST' and 'image' request.FILE:
        name = request.POST['name']
        age = request.POST['age']
        image = request.FILES['image']
        first = First(name=name, age=age, image=image)
        first.save()
        return HttpResponse('<h1>Success</h1>')
    context = {}
    return render(request, "index.html", context)
