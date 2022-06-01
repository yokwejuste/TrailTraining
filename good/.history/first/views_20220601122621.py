from django.shortcuts import render

def home(request):
    context={}
    return render("index.html", context)
