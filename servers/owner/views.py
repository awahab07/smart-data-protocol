from django.shortcuts import render

# Create your views here.

def index(request):
    context = None
    return render(request, 'owner/index.html', context)

def start(request):
    context = None
    return render(request, 'owner/start.html', context)
