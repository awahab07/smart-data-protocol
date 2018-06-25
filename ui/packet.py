import pyglet
from pyglet.gl import *

from .node import Node

from typing import List

class Packet:
    iconWidth =  50
    iconHeight = 50
    f = 1 / 60.0 # frame rate
    v = 10 # Velocity. Pixels / (1/60th sec)   i.e. pixels per frame to travel
    
    def __init__(self, icons: List[str] = []):
        self.batch = pyglet.graphics.Batch()
        self.sprites = []
        for i in range(len(icons)):
            x, y = i * self.iconWidth, self.iconHeight
            image = pyglet.resource.image(icons[i])
            image.width = self.iconWidth
            image.height = self.iconHeight
            self.sprites.append(pyglet.sprite.Sprite(image, x, y, batch=self.batch))

    def transmit(self, fromNode: Node, toNode: Node):
        #self.move(fromNode.image['x'], fromNode.image['y'])
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        print("transmit")
        #pyglet.clock.schedule_interval(self.animate, self.f)
        self.batch.draw()
        pass

    def animate(self, dt):
        for s in self.sprites:
            s.x += dt * self.v
            s.y += dt * self.v

    def move(self, x, y):
        width, height = 0, 0
        for s in self.sprites:
            s.x = x + width
            s.y = y + height
            width += self.iconWidth