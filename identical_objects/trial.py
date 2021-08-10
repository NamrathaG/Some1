from manim import *

class Indications(Scene):
    def construct(self):
        # indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        # names = [Tex(i.__name__).scale(3) for i in indications]
       

        colors = [DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E]
        radius = [1 + rad * 0.1 for rad in range(len(colors))]

        circles_group = VGroup()

        # zip(radius, color) makes the iterator [(radius[i], color[i]) for i in range(radius)]
        circles_group.add(*[Circle(radius=rad, stroke_width=10, color=col)
                            for rad, col in zip(radius, colors)])
        self.play(*[Create(Circle(radius=rad, stroke_width=10, color=RED)) for rad, col in zip(radius, colors)], *[Create(Circle(radius=rad+100, stroke_width=10, color=RED)) for rad, col in zip(radius, colors)], run_time =5)
        self.wait(5)

        # box = Group()
        # integer1 =  Integer(number=1).move_to([0,0,0]).scale(0.75)
        # integer2 = Integer(number =2 ).move_to([1,0,0]).scale(0.75)
        # box.add(integer1)
        # box.add(integer2)

        # # t = Text("hello there")
        # self.play(Indicate(box[0]), Indicate(box[1]))
        # self.wait(2)
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