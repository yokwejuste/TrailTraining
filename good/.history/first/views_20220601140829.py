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
            return HttpResponse("<h1>Thanks for your submission!</h1>")
    else:
        form = FirstForm()
    context = {
        'form': form,
    }
    return render(request, "index.html", context)


def result(request):
    student = First.objects.all()
    context = {
        'student': student
    }