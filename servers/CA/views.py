from django.shortcuts import render

# Create your views here.

def index(request):
    context = None
    return render(request, 'owner/index.html', context)

def resource(request, uid, resourceId):
    context = None
    return render(request, 'CA/index.html', context)
