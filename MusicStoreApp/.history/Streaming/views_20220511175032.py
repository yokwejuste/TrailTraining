from django.shortcuts import render
from .models import *


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")
        lecturer = request.POST.get("lecturer")
        form = Subjects(name= name, code=code, lecturer= lecturer)
        form.save()
        return H
    return render(request, 'index.html')
