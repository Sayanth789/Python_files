from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Circle
from manimlib.animation.creation import ShowCreation

class HelloCircle(Scene):
    def construct(self):
        circle = Circle()                # create a circle
        self.play(ShowCreation(circle))  # animate drawing the circle
        self.wait(1)                     # wait 1 second


        
