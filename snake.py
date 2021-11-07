from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((i*-20, 0))

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            new_heading = self.segments[seg_num - 1].heading()
            self.segments[seg_num].goto(new_xcor, new_ycor)
            self.segments[seg_num].setheading(new_heading)
        self.head.forward(20)

    def add_segment(self, position):
        tmp = Turtle("square")
        tmp.color("white")
        tmp.penup()
        tmp.goto(position)
        self.segments.append(tmp)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def goLeft(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def goRight(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def goUp(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def goDown(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)
