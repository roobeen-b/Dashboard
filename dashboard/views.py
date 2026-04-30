from django.shortcuts import render

def home(request):
    return render(request, 'dashboard.html')

def load(request):
    return render(request, 'loader.html')