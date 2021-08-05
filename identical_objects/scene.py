from manim import *
from itertools import permutations 

class MobjectExample(Scene):
    def construct(self):

        Red_coordinates = [ [-1,2,0],  [0,2,0], [1,2,0], [-1,1,0], [0, 1, 0], [1, 1, 0]]
        Blue_coordinates = [ [-1, 0 , 0],  [0,0,0] , [1, 0 , 0], [-1,-1,0], [0,-1,0]]
        Possible_outcomes = [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]
        positions_list = [1,2,3,4,5,6,7,8,9,10,11]
        Possible_outcomes2 = permutations(positions_list, 3) 
        box_of_circles = Group()
        box_of_circles2 = Group()

        # """
        # Box of balls
        # """
        index = 0
        box = Rectangle(width=3, height=4).move_to([0,0.5,0])
        text1 = MarkupText(f'6 <span fgcolor="{RED}">red</span> and 5 <span fgcolor="{BLUE}">blue</span> balls').shift(UP).shift(UP).shift(UP)
        box_of_circles.add(box)
        box_of_circles.add(text1)
        self.play(Create(box))
        self.play(Write(text1))
        for c in Red_coordinates:
        #     circle = Circle().scale(0.3)
        # circle.set_style(stroke_color=RED ,stroke_width=1,fill_opacity=0)
           circle = Circle().set_color(RED).scale(0.2).set_style(fill_opacity = 1).move_to(c)
           box_of_circles.add(circle)
           self.play(Create(circle), run_time = 0.5)
        #    self.play(Create(Dot(c).set_color(RED).scale(2)), run_time = 0.5)

        for c in Blue_coordinates: 
            circle = Circle().set_color(BLUE).scale(0.2).set_style(fill_opacity = 1).move_to(c)
            box_of_circles.add(circle)
            self.play(Create(circle), run_time = 0.5)
            # self.play(Create(Dot(c).set_color(BLUE).scale(2)), run_time = 0.5)

        self.wait(1)


        # """
        # So you are asked to pick 3 balls from this box without looking. What is the P(RRB) ?
        # """
        y = 3.5
        x = 4
        for outcome in Possible_outcomes:
            dot1 = Dot([x, y, 0])
            dot2 = Dot([x+1, y , 0])
            dot3 = Dot([x+2, y, 0])

            self.play(Create(dot1.set_color(RED if outcome[0] else BLUE).scale(2)), Create(dot2.set_color(RED if outcome[1] else BLUE).scale(2)), Create(dot3.set_color(RED if outcome[2] else BLUE).scale(2)))
            y = y - 1

        for a in box_of_circles:
             self.remove(a)

        # y = 3.5
        # x = 4
        # for outcome in Possible_outcomes:
        #     dot1 = Dot([x, y, 0])
        #     dot2 = Dot([x+1, y , 0])
        #     dot3 = Dot([x+2, y, 0])

        #     self.add(dot1.set_color(RED if outcome[0] else BLUE).scale(2), dot2.set_color(RED if outcome[1] else BLUE).scale(2), dot3.set_color(RED if outcome[2] else BLUE).scale(2))
        #     y = y - 1

        p1 = [3,3.5,0]
        p2 = [3,-3.5,0]
        brace = BraceBetweenPoints(p1,p2) 
        self.play(Create(brace))
        self.play(Write(Integer(8).next_to(brace, LEFT)))
        
        self.play(Create(Rectangle(width=4, height=1).move_to([5,-2.5,0])))
  
        # t1 = MathTex(r"\text{Probability} &= \frac{\text{number of favorable cases}}{\text{total number of cases}} \\ &= \frac{1}{8}").shift(LEFT*2)         
        t1 = MathTex(r"\text{prob(RRB)").shift(LEFT*3)
        t2 = MathTex(r"= \frac{\text{N(RRB)}}{\text{N(S)}}").next_to(t1)  
        t3 = MathTex(r"= \frac{1}{8}").next_to(t2, DOWN).align_to(t2,LEFT)       

        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Create(Cross(t3)))
        self.wait(5)

        self.clear()

        # """
        # This looks to be right, so what could have gone wrong.
        # Pause for a moment and see if you can figure out what went wrong.
        # """
        # #Pause screen

        # """
        # Okay so the devil is in the details. 
        # """
        t1 = MathTex(r"\text{Probability} = \frac{\text{number of favorable cases}}{\text{total number of cases}}")   
        t2 = MarkupText(f'Implicit in this definition is the assumption that each case is <span fgcolor="{YELLOW}">equally likely</span>').scale(0.5)
       
        self.play(Write(t1), run_time = 3)
        self.play(Write(t2.next_to(t1, DOWN)))

        self.clear()


        # """
        # Turns out our cases were not equally likely
        # """


        # """
        # Pause can you come up with a sample space such that all events in it are equally likely
        # """

        # """
        # Okay here's one
        # """
        box = Rectangle(width=3, height=4).move_to([0,0.5,0])
        box_of_circles2.add(box)
        self.play(Create(box))
        count = 1
        for c in Red_coordinates:
           integer =  Integer(number=count).move_to(c).scale(0.8)
           circle = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(c)
           box_of_circles2.add(integer)
           box_of_circles2.add(circle)
           self.play(Create(circle), Create(integer), run_time = 0.5)
           # self.play(Create(Dot(c).set_color(RED).scale(2)), run_time = 0.5)
           count = count +1 
        

        for c in Blue_coordinates: 
            integer =  Integer(number=count).move_to(c).scale(0.8)
            circle = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(c)
            box_of_circles2.add(integer)
            box_of_circles2.add(circle)
            self.play(Create(circle), Create(integer), run_time = 0.5)
            # self.play(Create(Dot(c).set_color(BLUE).scale(2)), run_time = 0.5)
            count = count + 1


        """
        Possible outcomes
        """

        y = 3.5
        x = 4
        count = 0
        for outcome in Possible_outcomes2:
            if count == 14:
                break  
            position1 = [x, y, 0]
            position2 = [x+1, y , 0]
            position3 = [x+2, y, 0]

            integer1 =  Integer(number=outcome[0]).move_to(position1).scale(0.8)
            circle1 = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(position1)
            
            integer2 =  Integer(number=outcome[1]).move_to(position2).scale(0.8)
            circle2 = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(position2)
            
            integer3 =  Integer(number=outcome[2]).move_to(position3).scale(0.8)
            circle3 = Circle().set_color(WHITE).scale(0.2).set_style(fill_opacity = 0,stroke_width=1).move_to(position3)
            
            
            self.play(Create(circle1), Create(integer1), Create(circle2), Create(integer2), Create(circle3), Create(integer3), run_time = 0.5)
            
            y = y - 0.5
            count = count +1

        self.play(Write(Text("...").move_to([x,y,0])))


        for a in box_of_circles2:
             self.remove(a)


        p1 = [3,3.5,0]
        p2 = [3,-3.5,0]
        brace = BraceBetweenPoints(p1,p2) 
        self.play(Create(brace))
        self.play(Write(Text("?").next_to(brace, LEFT)))


        """
        Better way to calculate total possible outcomes
        """
        pick1 = Line([-3,0,0], [-2,0,0])
        pick1_text = MarkupText(f"1<sup>st</sup> pick").next_to(pick1, DOWN).scale(0.5)
        choices1 = Integer(11).next_to(pick1, UP)
        pick2 = Line([-1.5, 0, 0] , [-0.5, 0,0])
        pick2_text = MarkupText(f"2<sup>nd</sup> pick").next_to(pick2, DOWN).scale(0.5)
        choices2 = Integer(10).next_to(pick2, UP)
        pick3 = Line([0,0,0],[1,0,0])
        pick3_text = MarkupText(f"3<sup>rd</sup> pick").next_to(pick3, DOWN).scale(0.5)
        choices3 = Integer(9).next_to(pick3, UP)
        self.play(Create(pick1), Create(pick2), Create(pick3))
        self.play(Write(pick1_text), Write(pick2_text), Write(pick3_text))
        self.play(Create(choices1), Create(choices2), Create(choices3))
        times1 = MathTex(r"\times").next_to(choices1 , buff=0.5)
        times2 = MathTex(r"\times").next_to(choices2 , buff=0.5)
        self.play(Write(times1), Write(times2))
        
        self.remove(pick1)
        self.remove(pick1_text)
        self.remove(choices1)
        self.remove(pick2)
        self.remove(pick2_text)
        self.remove(choices2)
        self.remove(pick3)
        self.remove(pick3_text)
        self.remove(choices3)
        self.remove(times1)
        self.remove(times2)

        """
        Similarly better way to calculate favourable outcomes
        """

        pick1 = Line([-3,0,0], [-2,0,0]).set_color(RED)
        pick1_text = MarkupText(f"1<sup>st</sup> pick").next_to(pick1, DOWN).scale(0.5)
        choices1 = Integer(6).next_to(pick1, UP)
        pick2 = Line([-1.5, 0, 0] , [-0.5, 0,0]).set_color(RED)
        pick2_text = MarkupText(f"2<sup>nd</sup> pick").next_to(pick2, DOWN).scale(0.5)
        choices2 = Integer(5).next_to(pick2, UP)
        pick3 = Line([0,0,0],[1,0,0]).set_color(BLUE)
        pick3_text = MarkupText(f"3<sup>rd</sup> pick").next_to(pick3, DOWN).scale(0.5)
        choices3 = Integer(5).next_to(pick3, UP)
        self.play(Create(pick1), Create(pick2), Create(pick3))
        self.play(Write(pick1_text), Write(pick2_text), Write(pick3_text))
        self.play(Create(choices1), Create(choices2), Create(choices3))
        self.play(Write(MathTex(r"\times").next_to(choices1 , buff=0.5)), Write(MathTex(r"\times").next_to(choices2 , buff=0.5)))
        
        self.clear()

        """
        Final answer
        """
        answer1 = MathTex(r"P(RRB) &= \frac{6 \times 5 \times 5}{11 \times 10 \times 9} \\ &= \frac{150}{990} \\ &= \frac{5}{33}")

        self.play(Write(answer1))
        
        
        
        

"""
TODO list
1. Add a box in the first screen
2. show that the right thing is to look at the no. of places
3. 

"""