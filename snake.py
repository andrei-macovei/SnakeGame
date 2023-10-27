from turtle import Turtle
import time

BOUNDS = 280

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.moves_until_update = 0

    def create_snake(self):
        for i in range(0, 3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(-20 * i, 0)
            self.segments.append(segment)

    def move(self):
        """Used for moving all segments part of the snake, one after the other"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].position())
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

    def enlarge(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.speed("fastest")
        segment.goto(self.segments[-1].pos())
        self.segments.append(segment)

    def manage_out_of_bounds_x(self):
        self.head.speed("fastest")
        if self.head.xcor() < -BOUNDS or self.head.xcor() > BOUNDS:
            self.head.goto(-self.head.xcor(), self.head.ycor())
        self.head.speed("normal")

    def manage_out_of_bounds_y(self):
        self.head.speed("fastest")
        if self.head.ycor() > BOUNDS or self.head.ycor() < -BOUNDS:
            self.head.goto(self.head.xcor(), -self.head.ycor())
        self.head.speed("normal")
