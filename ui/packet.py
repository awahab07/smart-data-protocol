import pyglet
from pyglet.gl import *

from .node import Node

from typing import List

class Packet:
    iconWidth =  50
    iconHeight = 50
    f = 1 / 60.0 # frame rate
    v = 1 # Velocity. Pixels / (1/60th sec)   i.e. pixels per frame to travel
    startTransmit = False
    directionX = 1 # Either 1 or -1 indicating direction of animation
    directionY = 1 # Either 1 or -1 indicating direction of animation
    
    def __init__(self, icons: List[str] = []):
        self.batch = pyglet.graphics.Batch()
        self.sprites = []
        for i in range(len(icons)):
            x, y = i * self.iconWidth, self.iconHeight
            image = pyglet.resource.image(icons[i])
            image.width = self.iconWidth
            image.height = self.iconHeight
            self.sprites.append(pyglet.sprite.Sprite(image, x, y, batch=self.batch))

        # Hiding all sprites at start
        self.hide()

    def draw(self):
        self.batch.draw()

    def hide(self):
        for s in self.sprites:
            s.visible = False

    def show(self):
        for s in self.sprites:
            s.visible = True

    def transmit(self, fromNode: Node, toNode: Node):
        if self.startTransmit == False:
            self.startTransmit = True
            self.directionX = 1 if toNode.image['x'] > fromNode.image['x'] else -1
            self.directionY = 1 if toNode.image['y'] > fromNode.image['y'] else -1
            self.move(fromNode.image['x'], fromNode.image['y'])
            self.show()
            pyglet.clock.schedule_interval(self.animate, self.f, fromNode, toNode)
            pass

    def animate(self, dt, fromNode: Node, toNode: Node):
        x2, y2, x1, y1 = toNode.image['x'], toNode.image['y'], self.sprites[0].x, self.sprites[0].y
        distanceFromTarget =  pow(pow(x2 - x1, 2) + pow(y2 - y1, 2), 1 / 2)
        if distanceFromTarget <= (self.iconWidth + self.iconHeight / 2):
            pyglet.clock.unschedule(self.animate)
            self.startTransmit = False
            self.hide()
        else:
            totalX = toNode.image['x'] - fromNode.image['x']
            totalY = toNode.image['y'] - fromNode.image['y']
            for s in self.sprites:
                s.x += dt * self.v * totalX
                s.y += dt * self.v * totalY

    def move(self, x, y):
        width, height = 0, 0
        for s in self.sprites:
            s.x = x + width
            s.y = y + height
            width += self.iconWidth
