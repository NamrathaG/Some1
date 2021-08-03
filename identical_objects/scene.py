from manim import *

# config.background_color = RED
# config.frame_y_radius = 5.0
# config.pixel_height = 500
# config.frame_height = 50
class MobjectExample(Scene):
    def construct(self):

        Red_coordinates = [ [-1,2,0],  [0,2,0], [1,2,0], [-1,1,0], [0, 1, 0], [1, 1, 0]]
        Blue_coordinates = [ [-1, 0 , 0],  [0,0,0] , [1, 0 , 0], [-1,-1,0], [0,-1,0]]
        # Possible_outcomes = [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]

        # self.play(Create(Rectangle(width=3, height=4).move_to([0,0.5,0])))
        # for c in Red_coordinates:
        # #     circle = Circle().scale(0.3)
        # # circle.set_style(stroke_color=RED ,stroke_width=1,fill_opacity=0)
        #    circle = Circle().set_color(RED).scale(0.2).set_style(fill_opacity = 1).move_to(c)
        #    self.play(Create(circle), run_time = 0.5)
        # #    self.play(Create(Dot(c).set_color(RED).scale(2)), run_time = 0.5)

        # for c in Blue_coordinates: 
        #     circle = Circle().set_color(BLUE).scale(0.2).set_style(fill_opacity = 1).move_to(c)
        #     self.play(Create(circle), run_time = 0.5)
        #     # self.play(Create(Dot(c).set_color(BLUE).scale(2)), run_time = 0.5)

        # self.clear()
        # self.wait(1)

           # circle = Circle().scale(0.3)
        # circle.set_style(stroke_color=RED ,stroke_width=1,fill_opacity=0)
        
        # self.add(circle, Integer(number=1))


        # self.play(Create(Rectangle(width=3, height=4).move_to([0,0.5,0])))
        # count = 1
        # for c in Red_coordinates:
        # #     circle = Circle().scale(0.3)
        # # circle.set_style(stroke_color=RED ,stroke_width=1,fill_opacity=0)
        #    integer =  Integer(number=count).move_to(c).scale(0.8)
        #    circle = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(c)
        #    self.play(Create(circle), Create(integer), run_time = 0.5)
        #    count = count +1 
        # #    self.play(Create(Dot(c).set_color(RED).scale(2)), run_time = 0.5)

        # for c in Blue_coordinates: 
        #     integer =  Integer(number=count).move_to(c).scale(0.8)
        #     circle = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(c)
        #     self.play(Create(circle), Create(integer), run_time = 0.5)
        #     count = count + 1
        #     # self.play(Create(Dot(c).set_color(BLUE).scale(2)), run_time = 0.5)


        pick1 = Line([-2,0,0], [-1,0,0])
        pick1_text = MarkupText(f"1<sup>st</sup> pick").next_to(pick1, DOWN).scale(0.5)
        choices1 = Integer(11).next_to(pick1, UP)
        pick2 = Line([-0.5, 0, 0] , [0.5, 0,0])
        pick2_text = MarkupText(f"2<sup>nd</sup> pick").next_to(pick2, DOWN).scale(0.5)
        choices2 = Integer(10).next_to(pick2, UP)
        pick3 = Line([1,0,0],[2,0,0])
        pick3_text = MarkupText(f"3<sup>rd</sup> pick").next_to(pick3, DOWN).scale(0.5)
        choices3 = Integer(9).next_to(pick3, UP)
        self.play(Create(pick1), Create(pick2), Create(pick3))
        self.play(Write(pick1_text), Write(pick2_text), Write(pick3_text))
        self.play(Create(choices1), Create(choices2), Create(choices3))
        self.play(Write(MathTex(r"\times").next_to(choices1 , buff=0.4)), Write(MathTex(r"\times").next_to(choices2 , buff=0.4)))

        self.wait(5)
        # text1 = MarkupText(f'6 <span fgcolor="{RED}">red</span> and 5 <span fgcolor="{BLUE}">blue</span> balls').shift(UP).shift(UP).shift(UP)

        # self.play(Write(text1))
        # self.remove(text1)

        # self.clear()
        # self.wait(1)


        # y = 3.5
        # x = 4
        # for outcome in Possible_outcomes:
        #     dot1 = Dot([x, y, 0])
        #     dot2 = Dot([x+1, y , 0])
        #     dot3 = Dot([x+2, y, 0])

        #     self.play(Create(dot1.set_color(RED if outcome[0] else BLUE).scale(2)), Create(dot2.set_color(RED if outcome[1] else BLUE).scale(2)), Create(dot3.set_color(RED if outcome[2] else BLUE).scale(2)))
        #     y = y - 1

        # self.play(Create(Rectangle(width=4, height=1).move_to([5,-2.5,0])))

        # self.play(Write(MathTex(r"\frac{1}{8}")))

        # self.clear()
        # self.wait(1)

        # t1 = MathTex(r"\text{Probability} = \frac{\text{number of favorable cases}}{\text{total number of cases}}")   
        # t2 = MarkupText(f'*Implicit in this definition is the assumption that each case is <span fgcolor="{YELLOW}">equally likely</span>').scale(0.5)
       
        # self.play(Write(t1), run_time = 3)
        # self.play(Write(t2.next_to(t1, DOWN)))


        # for c in Red_coordinates:
        #    self.play(Create(Dot(c).set_color(RED).scale(2)), run_time = 0.5)

        # for c in Blue_coordinates: 
        #     self.play(Create(Dot(c).set_color(BLUE).scale(2)), run_time = 0.5)

        # self.add(Dot([0,0,0]).set_opacity(0.2).set_stroke())

        # circle = Circle().scale(0.3)
        # circle.set_style(stroke_color=RED ,stroke_width=1,fill_opacity=0)
        
        # self.add(circle, Integer(number=1))
        
        # self.wait(5)

"""
TODO list
1. Add a box in the first screen
2. show that the right thing is to look at the no. of places
3. 

"""