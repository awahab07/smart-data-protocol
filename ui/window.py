import sys
import pyglet
from pyglet.gl import *

from .node import Node
from .packets import *

winProps = {
    'title': "Smart Data - Access Control",
    'width': 600,
    'height': 700,
    'padding': 10,
    'imageSize': 100
}

winProps['xCenter'] = winProps['width'] / 2
winProps['yCenter'] = winProps['height'] / 2


window = pyglet.window.Window(winProps['width'], winProps['height'], winProps['title'])

smartDataOwnerNode = Node('monitor.png', winProps['imageSize'], winProps['padding'], winProps['yCenter'], "Smart Data Owner")
requesterNode = Node('monitor.png', winProps['imageSize'], winProps['xCenter'] - winProps['imageSize'] / 2, winProps['height'] - winProps['padding'] - winProps['imageSize'], "Smart Data Requester")
cloudNode = Node('cloud.png', winProps['imageSize'], winProps['width'] - winProps['padding'] - winProps['imageSize'], winProps['yCenter'], "Cloud")

@window.event
def on_draw():
    window.clear()
    glEnable(GL_BLEND)

    # Drawing smartDataOwnerImage
    smartDataOwnerNode.draw()

    # Drawing smartDataOwnerImage
    requesterNode.draw()

    # Drawing cloudImage
    cloudNode.draw()

    smartDataOwnerAuthRequest.transmit(smartDataOwnerNode, cloudNode)

@window.event
def on_key_release(symbol, modifiers):
    smartDataOwnerAuthRequest.transmit(smartDataOwnerNode, cloudNode)

def show():
    window.set_visible()