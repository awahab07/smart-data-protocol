from django.shortcuts import render
from django.http import JsonResponse
import json

def index(request):
    postData = json.loads(request.body)
    
    data = {'success': True}
    # just return a JsonResponse
    return JsonResponse(data)
