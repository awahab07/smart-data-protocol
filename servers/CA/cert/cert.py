"""
Create certificates and private keys for the 'simple' example.
"""
from __future__ import print_function
import os
from pathlib import Path

from OpenSSL import crypto

from .certgen import createKeyPair, createCertRequest, createCertificate
from .validate_cert import verify_certificate_chain

CertificateError = crypto.X509StoreContextError

store_path = os.path.join((Path(os.path.dirname(__file__)).parent.parent), 'cert_store')
# Create Store Dir if not created
if not os.path.exists(store_path):
    os.mkdir(store_path)

def create_ca_cert(validity):
    cakey = createKeyPair(crypto.TYPE_RSA, 2048)
    careq = createCertRequest(cakey, CN='Certificate Authority')
    # CA certificate is valid for five years.
    cacert = createCertificate(careq, (careq, cakey), 0, (0, validity))

    print('Creating Certificate Authority private key in "CA.pkey"')
    with open(os.path.join(store_path, 'CA.pkey'), 'w') as capkey:
        capkey.write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, cakey).decode('utf-8')
        )

    print('Creating Certificate Authority certificate in "CA.cert"')
    with open(os.path.join(store_path, 'CA.cert'), 'w') as ca:
        ca.write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cacert).decode('utf-8')
        )

def create_server_cert(validity_after, validity_till,  cacert, cakey, cname):
    pkey = createKeyPair(crypto.TYPE_RSA, 2048)
    req = createCertRequest(pkey, CN=cname)
    # Certificates are valid for five years.
    cert = createCertificate(req, (cacert, cakey), 1, (validity_after, validity_till))

    print('Creating Certificate %s private key in "server.pkey"')
    with open(os.path.join(store_path, 'server.pkey'), 'w') as leafpkey:
        leafpkey.write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey).decode('utf-8')
        )

    print('Creating Certificate %s certificate in "server.cert"' % cname)
    with open(os.path.join(store_path, 'server.cert'), 'w') as leafcert:
        leafcert.write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode('utf-8')
        )

def create_requester_cert(valid_after_sec, valid_for_sec, user_name, user_id):
    try:
        ca_key, ca_cert = load(store_path, 'CA')
    except FileNotFoundError:
        raise Exception("ERROR: CA certificate not found")

    pkey = createKeyPair(crypto.TYPE_RSA, 2048)
    req = createCertRequest(pkey, CN=user_name)
    # Certificates are valid for five years.
    cert = createCertificate(req, (ca_cert, ca_key), 1, (valid_after_sec, valid_for_sec))

    print('Creating Resource Certificate %s private key in "%s.pkey"' % (user_name, user_id))
    with open(os.path.join(store_path, '%s.pkey') % (user_id), 'w') as leafpkey:
        leafpkey.write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey).decode('utf-8')
        )

    print('Creating Resource Certificate %s certificate in "%s.cert"' % (user_name, user_id,))
    with open(os.path.join(store_path, '%s.cert') % (user_id), 'w') as leafcert:
        leafcert.write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode('utf-8')
        )

def create_resource_cert(valid_after_sec, valid_for_sec, user_name, user_id, resource_id):
    try:
        ca_key, ca_cert = load(store_path, 'CA')
    except FileNotFoundError:
        raise Exception("ERROR: CA certificate not found")

    try:
        user_key, user_cert = load(store_path, user_id)
    except FileNotFoundError:
        raise Exception("ERROR: Requester certificate for user_name: %s user_id: %s not found" % (user_name, user_id))

    #pkey = createKeyPair(crypto.TYPE_RSA, 2048)
    req = createCertRequest(user_key, CN=user_name)
    cert = createCertificate(req, (ca_cert, ca_key), 1, (valid_after_sec, valid_for_sec))

    # print('Creating Resource Certificate %s private key in "%s_%s.pkey"' % (user_name, user_id, resource_id))
    # with open(os.path.join(store_path, '%s_%s.pkey') % (user_id, resource_id), 'w') as leafpkey:
    #     leafpkey.write(
    #         crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey).decode('utf-8')
    #     )

    print('Creating Resource Certificate %s certificate in "%s_%s.cert"' % (user_name, user_id, resource_id))
    with open(os.path.join(store_path, '%s_%s.cert') % (user_id, resource_id), 'w') as leafcert:
        leafcert.write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode('utf-8')
        )

def ca_cert_exists():
    if (not os.path.exists(os.path.join(store_path, 'CA.cert'))):
        raise FileNotFoundError()
    return True

def verify_requester_cert(user_id):
    cert_path = os.path.join(store_path, '%s.cert') % (user_id)
    trusted_certs = [os.path.join(store_path, 'CA.cert')]

    cert_valid = verify_certificate_chain(cert_path, trusted_certs)

    if not cert_valid:
        print("Invalid certificate!")
    return cert_valid


def verify_resource_cert(user_id, resource_id):
    """
    Verifies whether a resource cert exists and is valid
    :param user_id: User unique identifier requesting resource
    :param resource_id: Resource unique identifier
    :return: boolean
    """
    cert_path = os.path.join(store_path, '%s_%s.cert') % (user_id, resource_id)
    trusted_certs = [os.path.join(store_path, 'CA.cert'), os.path.join(store_path, '%s.cert' % user_id)]

    cert_valid = verify_certificate_chain(cert_path, trusted_certs)

    if not cert_valid:
        print("Invalid certificate!")
    return cert_valid


def load(store_path, domain):
    cert = open(os.path.join(store_path, domain + ".cert"))
    pkey = open(os.path.join(store_path, domain + ".pkey"))

    result = (
        crypto.load_privatekey(crypto.FILETYPE_PEM, pkey.read()),
        crypto.load_certificate(crypto.FILETYPE_PEM, cert.read()))
    cert.close()
    pkey.close()
    return result
