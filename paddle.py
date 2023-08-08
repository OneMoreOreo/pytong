from turtle import Turtle


UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.coloring = "darkorange1"
        self.shapez = 'square'
        self.position = position
        self.create_paddle()


    def create_paddle(self):

        self.penup()
        self.color(self.coloring)
        self.shape(self.shapez)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.goto(self.position)


    def up(self):

        self.forward(20)
    def down(self):

        self.backward(20)







