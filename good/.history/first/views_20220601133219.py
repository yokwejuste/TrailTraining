from django.http import HttpResponse
from django.shortcuts import render

from first.forms import FirstForm
from .models import *

def home(request):
    if request.method == 'POST':
        form = FirstForm(request.PO
        ST, request.FILES)
    context = {}
    return render(request, "index.html", context)
