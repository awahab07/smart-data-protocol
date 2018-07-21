import pyglet
from pyglet.gl import *

from .node import Node
from .packet import Packet

from typing import List

icons = {
    'authRequest': 'user-auth-request.png',
    'userCertificate': 'certificate.png',
    'questionMark': 'question-mark.png',
    'tickMark': 'tick-mark.png',
    'userAuthToken': 'user-auth-token.png',
    'accessRuleCheck': 'access-rule-check.png',
    'initializing': 'initializing.png',
    'accessDenied': 'access-denied.png',
    'accessGranted': 'access-granted.png',
    'folder': 'folder.png',
    'folderAccessGranted': 'folder-access-granted.ico',
    'folderAccessDenied': 'folder-access-denied.ico',
    'folderUpload': 'folder-upload.ico',
    'notification': 'notification.png'
}

smartDataOwnerAuthRequest = Packet([icons['authRequest'], icons['userCertificate']])
userAuthToken = Packet([icons['userAuthToken']])

protocolPackets = {
    'REQUESTER_INITIALIZING': {'packet': Packet([icons['initializing']]), 'from': 'requesterNode', 'to': 'centerNode'},
    'REQUESTER_AUTH_REQUEST': {'packet': Packet([icons['authRequest'], icons['userCertificate']]), 'from': 'requesterNode', 'to': 'cloudNode'},
    'REQUESTER_AUTHENTICATED': {'packet': Packet([icons['userAuthToken'], icons['userCertificate']]), 'from': 'cloudNode', 'to': 'requesterNode'},

    'REQUESTER_WHETHER_AUTHORIZED': {'packet': Packet([icons['userCertificate'], icons['questionMark']]), 'from': 'requesterNode', 'to': 'authorizationServerNode'},
    'REQUESTER_IS_AUTHORIZED': {'packet': Packet([icons['userAuthToken'], icons['tickMark']]), 'from': 'authorizationServerNode', 'to': 'requesterNode'},

    'REQUESTER_RESOURCE_ACCESS': {'packet': Packet([icons['accessRuleCheck']]), 'from': 'requesterNode', 'to': 'userAccessRulesNode'},
    'REQUESTER_RESOURCE_ACCESS_DENIED': {'packet': Packet([icons['accessDenied']]), 'from': 'userAccessRulesNode', 'to': 'requesterNode'},
    'REQUESTER_RESOURCE_ACCESS_GRANTED': {'packet': Packet([icons['accessGranted']]), 'from': 'userAccessRulesNode', 'to': 'requesterNode'},

    'REQUESTER_RESOURCE_CHANGE_REQUEST': {'packet': Packet([icons['folder']]), 'from': 'requesterNode', 'to': 'userAccessRulesNode'},
    'REQUESTER_RESOURCE_CHANGE_REQUEST_DENIED': {'packet': Packet([icons['folderAccessDenied']]), 'from': 'userAccessRulesNode', 'to': 'requesterNode'},
    'REQUESTER_RESOURCE_CHANGE_REQUEST_GRANTED': {'packet': Packet([icons['folderAccessGranted']]), 'from': 'userAccessRulesNode', 'to': 'requesterNode'},

    'OWNER_INITIALIZING': {'packet': Packet([icons['initializing']]), 'from': 'smartDataOwnerNode', 'to': 'centerNode'},
    'OWNER_AUTH_REQUEST': {'packet': Packet([icons['authRequest'], icons['userCertificate']]), 'from': 'smartDataOwnerNode', 'to': 'cloudNode'},
    'OWNER_AUTHENTICATED': {'packet': Packet([icons['userAuthToken'], icons['userCertificate']]), 'from': 'cloudNode', 'to': 'smartDataOwnerNode'},
    'OWNER_FILE_UPLOAD': {'packet': Packet([icons['folderUpload']]), 'from': 'smartDataOwnerNode', 'to': 'cloudNode'},
    'OWNER_NOTIFIED': {'packet': Packet([icons['notification']]), 'from': 'gatewayNode', 'to': 'smartDataOwnerNode'}
}

def drawPackets():
    for key in protocolPackets.keys():
        protocolPackets[key]['packet'].draw()

    smartDataOwnerAuthRequest.draw()
    userAuthToken.draw()
