from manim import *

class Indications(Scene):
    def construct(self):

        Possible_outcomes = [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]

        y = 3.5
        x = 4
        for outcome in Possible_outcomes:
            pos1 = [x, y, 0]
            pos2 = [x+1, y , 0]
            pos3 = [x+2, y, 0]
            
            circle1 = Circle().set_color(RED if outcome[0] else BLUE).scale(0.2).move_to(pos1).set_style(fill_opacity = 1)
            circle2 = Circle().set_color(RED if outcome[1] else BLUE).scale(0.2).move_to(pos2).set_style(fill_opacity = 1)
            circle3 = Circle().set_color(RED if outcome[2] else BLUE).scale(0.2).move_to(pos3).set_style(fill_opacity = 1)
            self.add(circle1)
            self.add(circle2)
            self.add(circle3)
            y = y - 1



        
        self.play(Create(Rectangle(width=4, height=1).move_to([5,3.5,0])), Create(Rectangle(width=4, height=1).move_to([5,-3.5,0])), run_time=2)

        self.wait(5)

        text = MarkupText(f'P(<span fgcolor="{RED}">RRR</span>) > P(<span fgcolor="{BLUE}">BBB</span>)')
        self.play(Write(text), run_time=2)


        # indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        # names = [Tex(i.__name__).scale(3) for i in indications]
        # self.wait(1)
        # self.add(Circle().move_to([0,0,0]))
        # self.wait(1) 
        # self.add(Circle().move_to([1,0,0]))
        # self.wait(1)
        # colors = [DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E]
        # radius = [1 + rad * 0.1 for rad in range(len(colors))]

        # circles_group = VGroup()

        # # zip(radius, color) makes the iterator [(radius[i], color[i]) for i in range(radius)]
        # circles_group.add(*[Circle(radius=rad, stroke_width=10, color=col)
        #                     for rad, col in zip(radius, colors)])
        # circleslist = [Circle(radius=rad, stroke_width=10, color=col) for rad, col in zip(radius, colors)]
   
        # self.play(*[Create(l) for l in circleslist], run_time =5)
        # self.wait(5)
        
        # for k in circleslist: 
        #     self.remove(k)
        

        # t = Text("hello there")
        # self.play(Write(t))
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