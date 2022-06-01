from django.shortcuts import render
from .models import *

def home(request):
    if request.method == 'POST' and 'image' in request.FILES:
        name = request.POST['name']
        age = request.POST['age']
        image = request.FILES['image']
        first = First(name=name, age=age, )
        first.save()
    context = {}
    return render(request, "index.html", context)
