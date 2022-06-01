from email.errors import FirstHeaderLineIsContinuationDefect
from django.http import HttpResponse
from django.shortcuts import render

from first.forms import FirstForm
from .models import *

def home(request):
    form = FirstForm()
    if request.method == 'POST':
        form = FirstForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        
    }
    return render(request, "index.html", context)
