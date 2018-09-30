from django.shortcuts import render
from django.http import JsonResponse

from .cloud import cloud

from .cert import cert

def index(request):
    context = None
    return render(request, 'owner/index.html', context)

def resource(request, uid, resourceId):
    try:
        cert.ca_cert_exists()
    except FileNotFoundError:
        return respondWithCertificateError(request, 'Certificate Error', 'CA certificate could not be found.')

    try:
        cert.verify_requester_cert(uid)
    except FileNotFoundError:
        return respondWithCertificateError(request, 'Certificate Error', 'Requester certificate could not be found.')
    except cert.CertificateError as ce:
        return respondWithCertificateError(request, 'Requester Certificate', str(ce))

    try:
        cert.verify_resource_cert(uid, resourceId)
    except FileNotFoundError:
        cloud.insert_resource_certificate_request(uid, resourceId)
        return respondWithCertificateError(request, 'Certificate Error', 'Resource certificate for this requester could not be found.' + ' Owner of the resource will be requested for permission.')
    except cert.CertificateError as ce:
        cloud.insert_resource_certificate_request(uid, resourceId)
        return respondWithCertificateError(request, 'Resource Access', str(ce) + ' Owner of the resource will be requested for permission.')

    cloud.fire_message('REQUESTER_RESOURCE_ACCESS_GRANTED', "Certificate validation - Success")
    cloud.mark_resource_accessed(resourceId)

    return render(request, 'CA/resource.html', {'resourceUrl': cloud.get_resource_url(resourceId)})

def respondWithCertificateError(request, title, message):
    cloud.fire_message('REQUESTER_RESOURCE_ACCESS_DENIED', "Certificate validation - FAILED")
    return render(request, 'CA/error.html', {'title': title, 'message': message})
