from turtle import Turtle


class Ball(Turtle):
    def __init__(self) :
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.up()
        self.incy = 10
        self.incx = 10

    def move(self):
        new_x = self.xcor() + self.incx
        new_y = self.ycor() + self.incy
        self.goto(new_x,new_y)
    
    def bounce(self):
        self.incy *= -1

    def bounce_paddle(self):
        self.incx *= -1

    def resetpos(self):
        self.goto(0,0)
        self.bounce_paddle()