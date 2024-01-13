from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_list = []
        # segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake_list.append(new_segment)

    def extend(self):
        self.add_snake(self.snake_list[-1].position())


    def move(self):
        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x,
                                          new_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    def reset_snake(self):
        for snake in self.snake_list:
            snake.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.snake_list[0].heading()

    def up(self):
        if self.snake_list[0].heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def down(self):
        if self.snake_list[0].heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def left(self):
        if self.snake_list[0].heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)

    def right(self):
        if self.snake_list[0].heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)
