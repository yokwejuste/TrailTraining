from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {}
    return HttpResponse
    return render("index.html", context)
