import pyglet
from pyglet import shapes
import numpy as np
from model import TinyNN

window = pyglet.window.Window(800, 600)

nn = TinyNN()

batch = pyglet.graphics.Batch()   

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

nodes = {
    "input": [(200, 150), (200, 300)],
    "hidden": [(400, 100), (400, 250), (400, 400)],
    "output": [(600, 250)]
}

def update(dt):
    nn.train_step(X, y, lr=0.1)

pyglet.clock.schedule_interval(update, 0.1)

@window.event
def on_draw():
    window.clear()

    # clear previous batch contents safely
    batch = pyglet.graphics.Batch()

    # neurons
    for layer in nodes.values():
        for x, y in layer:
            shapes.Circle(x, y, 20, batch=batch)

    # connections
    for i, (x1, y1) in enumerate(nodes["input"]):
        for j, (x2, y2) in enumerate(nodes["hidden"]):
            shapes.Line(x1, y1, x2, y2, batch=batch)

    batch.draw()

pyglet.app.run()