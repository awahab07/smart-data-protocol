import pyglet
from pyglet.window import Screen

pyglet.resource.path = ['images/']
pyglet.resource.reindex()

from ui import window

# Positioning window
defaultScreen = pyglet.window.get_platform().get_default_display().get_default_screen()
windowWidth, y = window.getSize()
window.position(int((defaultScreen.width - windowWidth) / 2), 20)

pyglet.app.run()

