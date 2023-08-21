from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for positions in STARTING_POSITIONS:
            self.add_segments(positions)

    def add_segments(self, pos):
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.penup()
        new_segment.shape("square")
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def increase(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, - 1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

