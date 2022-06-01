from django.shortcuts import render
from .models import *


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        code = request.POST.get("code")name
        lecturer = request.POST.get("lecturer")
        form = Subjects(name= )
    return render(request, 'index.html')
