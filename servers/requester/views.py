from django.shortcuts import render

# Create your views here.
def index(request):
    context = None
    return render(request, 'requester/index.html', context)

def start(request):
    context = None
    return render(request, 'requester/start.html', context)