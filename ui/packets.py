import pyglet
from pyglet.gl import *

from .node import Node
from .packet import Packet

from typing import List

icons = {
    'authRequest': 'user-auth-request.png',
    'userCertificate': 'certificate.png',
    'userAuthToken': 'user-auth-token.png'
}

smartDataOwnerAuthRequest = Packet([icons['authRequest'], icons['userCertificate']])
userAuthToken = Packet([icons['userAuthToken']])

def drawPackets():
    smartDataOwnerAuthRequest.draw()
    userAuthToken.draw()
