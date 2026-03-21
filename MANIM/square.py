from manimlib.scene.scene import Scene 
from manimlib.mobject.geometry import Square
from manimlib.animation.creation import ShowCreation


class HelloSquare(Scene):
    def construct(self):
        square = Square() 
        self.play(ShowCreation(square))
        self.wait(1)