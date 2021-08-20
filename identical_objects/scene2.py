from manim import *
from itertools import permutations 
import random

def random_derangement(n):
        while True:
            v = [i for i in range(n)]
            for j in range(n - 1, -1, -1):
                p = random.randint(0, j)
                if v[p] == j:
                    break
                else:
                    v[j], v[p] = v[p], v[j]
            else:
                if v[0] != 0:
                    return tuple(v)

class MobjectExample(Scene):
    def construct(self):

        coordinates  = [[-1, 2, 0],  [0, 2, 0], [1, 2, 0], [-1, 1, 0], [0, 1, 0], [1, 1, 0], [-1, 0, 0], [0, 0, 0] , [1, 0 , 0], [-1, -1, 0], [0, -1, 0]]
        colors  = [RED, RED, RED, RED, RED, RED, BLUE, BLUE, BLUE, BLUE, BLUE]
        word = ["Hello", "Hello", "Hello", "Hello", "Hello", "Hello", "World", "World", "World", "World", "World"]
        indices = [0,1,2,3,4,5,6,7,8,9,10]
        Possible_outcomes = [[0,0], [0,1], [1,0], [1,1]]
        box_of_wt = VGroup()
        box_of_words = VGroup()
        box_of_tiles = VGroup()
    
        box = Rectangle(width=3, height=4).move_to([0,0.5,0])
        text1 = MarkupText(f'6 <span fgcolor="{RED}">Hello</span> and 5 <span fgcolor="{BLUE}">World</span> tiles').shift(UP).shift(UP).shift(UP).scale(0.7)
        self.play(Create(box))
        self.play(Write(text1))

        words = [Text(wor, color=col).scale(0.3).move_to(cor) for cor, col, wor in zip(coordinates, colors, word)]
        questionmarks = [Text("?").scale(0.3).move_to(cor) for cor in coordinates]
        tiles = [Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(cor).set_stroke(width=1) for cor, col in zip(coordinates, colors)]
       
        for w,r in zip(words,tiles): 
            k = VGroup()
            k.add(r,w)
            box_of_wt.add(k)
            box_of_words.add(w)
            box_of_tiles.add(r)
        

        self.play(*[Create(b) for b in box_of_tiles], run_time = 2)
        self.add(*[b for b in box_of_words])
        self.wait(2)
        self.play(*[b.animate.flip() for b in box_of_tiles], *[Transform(a, b) for a, b in zip(box_of_words, questionmarks)])
        self.wait(2)
        random.shuffle(indices)
        # shuffled_indices = random_derangement(11)
        self.play(*[b.animate.move_to(coordinates[i]) for b, i in zip(box_of_wt, indices) ], run_time =1)
        random.shuffle(indices)
        self.play(*[b.animate.move_to(coordinates[i]) for b, i in zip(box_of_wt, indices) ], run_time =1)

       
        self.wait(5)


        text2 = MarkupText(f'P(<span fgcolor="{RED}">Hello</span><span fgcolor="{BLUE}">World</span>) = ?').next_to(box,DOWN, buff=0.5).scale(0.7)
        self.play(Write(text2))
        
        self.wait(2)



        """
        Let's look at all the possible outcomes. 
        
        """
        y = 1.5
        x = 4
        for outcome in Possible_outcomes:
            pos1 = [x, y, 0]
            pos2 = [x+1, y , 0]
            pos3 = [x+2, y, 0]
            

            words = [Text(wor, color=col).scale(0.3).move_to(cor) for cor, col, wor in zip(coordinates, colors, word)]
            
            tile1 = Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(pos1).set_stroke(width=1)
            tile2 = Rectangle().set_fill(GRAY, opacity=0.2).scale(0.2).move_to(pos2).set_stroke(width=1)
            word1 = Text("Hello" if outcome[0] else "World").set_color(RED if outcome[0] else BLUE).scale(0.3).move_to(pos1)
            word2 = Text("Hello" if outcome[1] else "World").set_color(RED if outcome[1] else BLUE).scale(0.3).move_to(pos2)
            self.play(Create(tile1), Write(word1))
            self.play(Create(tile2), Write(word2))
            y = y - 1


        # TODO: Write pick1 and pick2 on the sample space
        ellipse_1 = Ellipse(width=3, height=5, color=BLUE_B).move_to([4.5, 0,0])
        self.play(Create(ellipse_1))
        self.wait(5)
        # for a in box_of_circles:
        #      self.remove(a)

        # p1 = [3,3.5,0]
        # p2 = [3,-3.5,0]
        # brace = BraceBetweenPoints(p1,p2) 
        # self.play(Create(brace))
        # self.play(Write(Integer(8).next_to(brace, LEFT)))
        
        # self.play(Create(Rectangle(width=4, height=1).move_to([5,-2.5,0])))