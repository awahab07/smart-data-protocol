import sys
import pyglet
from pyglet.gl import *

from .node import Node
from .packets import *
from cefpython3 import cefpython as cef

winProps = {
    'title': "Smart Data - Access Control",
    'width': 900,
    'height': 700,
    'padding': 10,
    'imageSize': 100,
    'fps': 1 / 60.0
}

winProps['xCenter'] = winProps['width'] / 2
winProps['yCenter'] = winProps['height'] / 2


window = pyglet.window.Window(winProps['width'], winProps['height'], winProps['title'])

smartDataOwnerNode = Node('monitor.png', winProps['imageSize'], winProps['padding'], winProps['yCenter'], "Smart Data Owner")
requesterNode = Node('monitor.png', winProps['imageSize'], winProps['xCenter'] - winProps['imageSize'] / 2, winProps['height'] - winProps['padding'] - winProps['imageSize'], "Smart Data Requester")
cloudNode = Node('cloud.png', winProps['imageSize'], winProps['width'] - winProps['padding'] - winProps['imageSize'], winProps['yCenter'], "Cloud")

# Initializing gateway node and associated authorization and access rule nodes
gatewayNode = Node('gateway.png', winProps['imageSize'], winProps['xCenter'] - winProps['imageSize'] / 2, 2 * winProps['padding'] + winProps['imageSize'], "Gateway")
authorizationServerNode = Node('authorization-server.png', winProps['imageSize'], winProps['xCenter'] - (winProps['imageSize'] * 2.5), winProps['padding'], "Authorization Server")
userAccessRulesNode = Node('access-rule-component.png', winProps['imageSize'], winProps['xCenter'] + (winProps['imageSize'] * 1.5), winProps['padding'], "User Access Rule Component")

# Initializing connecting lines
connecting_lines_batch = pyglet.graphics.Batch()
connecting_lines_batch.add(2, pyglet.gl.GL_LINES, None, ('v2f', (authorizationServerNode.getCenter()['x'], gatewayNode.getCenter()['y'], userAccessRulesNode.getCenter()['x'], gatewayNode.getCenter()['y'])))
connecting_lines_batch.add(2, pyglet.gl.GL_LINES, None, ('v2f', (authorizationServerNode.getCenter()['x'], gatewayNode.getCenter()['y'], authorizationServerNode.getCenter()['x'], authorizationServerNode.getCenter()['y'] + 40)))
connecting_lines_batch.add(2, pyglet.gl.GL_LINES, None, ('v2f', (userAccessRulesNode.getCenter()['x'], gatewayNode.getCenter()['y'], userAccessRulesNode.getCenter()['x'], userAccessRulesNode.getCenter()['y'] + 40)))

# Status Label
statusLabel = pyglet.text.Label("", font_name='Aria', font_size=12, bold=True, x = winProps['xCenter'], y = winProps['yCenter'], anchor_x='center',  anchor_y='center', multiline=True, width=winProps['width'] / 4, align='center')

def update_frames(dt):
    userAuthToken.transmit(cloudNode, smartDataOwnerNode)
    pass

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

    # Drawing lines to connect gateway with authorization server and user access rules component
    connecting_lines_batch.draw()

    # Drawing gatewayNode
    gatewayNode.draw()

    # Drawing authorization server
    authorizationServerNode.draw()

    # Drawing user access rules component
    userAccessRulesNode.draw()

    # Drawing status label
    statusLabel.draw()

    # Drawing requests that will depict data transmission
    drawPackets()

    # Calling update frames every 60th of a second (Effectually creating a 60 fps).
    pyglet.clock.schedule_interval(update_frames, winProps['fps'])


@window.event
def on_key_release(symbol, modifiers):
    if symbol == 49: # key "1"
        smartDataOwnerAuthRequest.transmit(smartDataOwnerNode, cloudNode)
        statusLabel.text = "Sending user Authentication Request + Certificate"
    if symbol == 50: # key "2"
        userAuthToken.transmit(cloudNode, smartDataOwnerNode)
        statusLabel.text = "User Authenticated. Sending [Auth Ticket]"
    pass

def show():
    window.set_visible()

def position(x, y):
    window.set_location(x, y)

def getSize():
    return [winProps['width'], winProps['height']]

def log(msg):
    statusLabel.text = "Message Received"

