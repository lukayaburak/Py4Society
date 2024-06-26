from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for position in STARTING_POSITIONS:
            newSegment = Turtle("square")
            newSegment.color("white")
            newSegment.penup()
            newSegment.goto(position)
            self.segments.append(newSegment)

    def move(self):
        for segmentNumb in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segmentNumb - 1].xcor()
            new_y = self.segments[segmentNumb - 1].ycor()
            self.segments[segmentNumb].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def addSegment(self,pos):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(pos)
        self.segments.append(newSegment)

    def extend(self):
        self.addSegment(self.segments[-1].position())
