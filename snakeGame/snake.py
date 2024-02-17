from turtle import Turtle, Screen
Move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
Positions = [(0,0), (-20, 0), (-40, 0), (-60, 0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in Positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
                x_cor = self.segments[i - 1].xcor()
                y_cor = self.segments[i - 1].ycor()
                self.segments[i].goto(x_cor, y_cor)
        self.segments[0].forward(Move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]










