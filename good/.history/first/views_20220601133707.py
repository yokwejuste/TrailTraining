from email.errors import FirstHeaderLineIsContinuationDefect
from django.http import HttpResponse
from django.shortcuts import render

from first.forms import FirstForm
from .models import *

def home(request):
    if request.method == 'POST':
        form = FirstForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    else:
        formFirstForm()
    context = {
        'form': form,
    }
    return render(request, "index.html", context)
