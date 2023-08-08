from turtle import Turtle



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color("cyan")
        self.shapesize(stretch_len=1.2,stretch_wid=1.2)
        self.goto(0,0)
        # self.setheading(45)
        self.x_dir = 10
        self.y_dir = 10
        self.move_speed = 0.1

    def move(self):
    # def move(self,dir):
        # direction = dir
        x = self.xcor()+self.x_dir
        y = self.ycor()+self.y_dir
        # y = self.ycor()+10*(direction)
        self.goto(x,y)
        # self.goto(x+15,y+10)
        # degree = 45
        # self.setheading(degree)
        # self.forward(15)

    def bounce_y(self):
        self.y_dir*=-1
    
    def bounce_x(self):
        self.x_dir*=-1
        self.move_speed *= 0.8
        # self.move_speed /= 2

    def reset_match(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce_x()

        



