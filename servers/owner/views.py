from django.shortcuts import render
from django.http import JsonResponse

import sys, json

sys.path.append("..")

from CA.cert import cert
from CA.cloud import cloud

def index(request):
    context = None
    return render(request, 'owner/index.html', context)

def start(request):
    context = None
    return render(request, 'owner/start.html', context)

def request_resource_access(request):
    """
    This will generate resource access certificate for a given user
    :return:
    """
    try:
        postedJSON = json.loads(request.body)
        valid_after_sec = postedJSON['validAfter']
        valid_for_sec = postedJSON['validFor']
        user_name = postedJSON['userName']
        uid = postedJSON['userId']
        resource_id = postedJSON['resourceId']
        result = cert.create_resource_cert(valid_after_sec, valid_for_sec, user_name, uid, resource_id)
        # Deleting cloud record
        cloud.delete_resource_certificate_request(uid, resource_id)

        # Firing resource cert successful event
        cloud.fire_message('RESOURCE_CERTIFICATE_CREATED', "Resource Certificate - Generated")
        cloud.fire_message('RESOURCE_CERTIFICATE_GENERATED', "Resource Certificate - Generated")
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': True, 'message': str(result)})
