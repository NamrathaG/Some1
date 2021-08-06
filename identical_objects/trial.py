from manim import *

class Indications(Scene):
    def construct(self):
        # indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        # names = [Tex(i.__name__).scale(3) for i in indications]
       

        box = Group()
        integer1 =  Integer(number=1).move_to([0,0,0]).scale(0.75)
        integer2 = Integer(number =2 ).move_to([1,0,0]).scale(0.75)
        box.add(integer1)
        box.add(integer2)

        # t = Text("hello there")
        self.play(Indicate(box[0]), Indicate(box[1]))
        self.wait(2)
        # self.add(names[0])
        # for i in range(len(names)):
        #     if indications[i] is Flash:
        #         self.play(Flash(UP))
        #     elif indications[i] is ShowPassingFlash:
        #         self.play(ShowPassingFlash(Underline(names[i])))
        #     else:
        #         self.play(indications[i](names[i]))
        #     self.play(AnimationGroup(
        #         FadeOut(names[i], shift=UP*1.5),
        #         FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
        #     ))