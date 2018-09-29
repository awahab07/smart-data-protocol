from django.shortcuts import render

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
        return respondWithCertificateError(request, 'Requester Certificate', ce[2])

    try:
        cert.verify_resource_cert(uid, resourceId)
    except FileNotFoundError:
        return respondWithCertificateError(request, 'Certificate Error', 'Resource certificate for this requester could not be found.')
    except cert.CertificateError as ce:
        return respondWithCertificateError(request, 'Resource Access', ce[2])

    context = {'title': "Title", 'message': "Message"}
    return render(request, 'CA/error.html', context)

def respondWithCertificateError(request, title, message):
    return render(request, 'CA/error.html', {'title': title, 'message': message})
