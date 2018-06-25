import pyglet
from pyglet.gl import *

from .node import Node
from .packet import Packet

from typing import List

icons = {
    'authRequest': 'user-auth-request.png',
    'userCertificate': 'certificate.png'
}

smartDataOwnerAuthRequest = Packet([icons['authRequest'], icons['userCertificate']])