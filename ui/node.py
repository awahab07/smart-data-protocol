import pyglet
from pyglet.gl import *

class Node:
    def init(self):
        self.image = {
            'url': "",
            'x': 0,
            'y': 0,
            'width': 100,
            'height': 100,
            'instance': None
        }

        self.label = {
            'text': "",
            'x': 0,
            'y': 0,
            'instance': None
        }

    labelHeight = 20

    def __init__(self, imageUrl = "", imageSize = 100, x = 0, y = 0, label = ""):
        self.init()

        self.image['url'] = imageUrl
        self.image['x'] = x
        self.image['y'] = y
        self.image['width'] = imageSize
        self.image['height'] = imageSize
        self.image['instance'] = pyglet.resource.image(self.image['url'])
        self.image['instance'].width = imageSize
        self.image['instance'].height = imageSize

        # Assigning and calculating label position
        self.label['text'] = label
        self.label['x'] = self.image['x']
        self.label['y'] = self.image['y'] - self.labelHeight
        
        self.label['instance'] = pyglet.text.Label(self.label['text'],
                          font_name='Aria',
                          font_size=12,
                          x = self.label['x'], 
                          y = self.label['y'],
                          anchor_x='left', 
                          anchor_y='center',
                          multiline=True,
                          width=self.image['width'],
                          align='center')

    def draw(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.image['instance'].blit(self.image['x'], self.image['y'])
        self.label['instance'].draw()

    def getCenter(self):
        return dict(x = self.image['x'] + self.image['width'] / 2, y = self.image['y'] + self.image['height'] / 2)

    def blink(self):
        # Initializing connecting lines
        highlightBatch = pyglet.graphics.Batch()
        highlightBatch.add(2, pyglet.gl.GL_LINES, None, ('v2f', (self.image['x'], self.image['y'], self.image['x'] + self.image['width'], self.image['y'] + self.image['height'])))
        highlightBatch.add(2, pyglet.gl.GL_LINES, None, ('v2f', (self.image['x'] + self.image['width'], self.image['y'], self.image['x'] + self.image['width'], self.image['y'] + self.image['height'])))

