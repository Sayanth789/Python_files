from manimlib.scene.scene import Scene
from manimlib.mobject.svg.text_mobject import Text
from manimlib.animation.creation import ShowCreation

class HelloText(Scene):
    def construct(self):
        t = Text("Hello I'm the DEATH!")  # use Text instead of TextMobject
        self.play(ShowCreation(t))
        self.wait(1)