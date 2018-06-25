import pyglet

pyglet.resource.path = ['images/']
pyglet.resource.reindex()

from ui import window

#window.show()

pyglet.app.run()

