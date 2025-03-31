import math
from abc import ABC


class shape(ABC):
    def __init__(self, color, movement_speed, blocks):
        self.color = color
        self.movement_speed = movement_speed
        self.blocks = blocks

    def transpose(self, direction):
        x_center, y_center = self.blocks[0].x, self.blocks[0].y
        if direction == "up":
            for block in self.blocks:
                x = block.x
                y = block.y
                block.set_x(x_center + int(y - y_center))
                block.set_y(y_center - x + x_center)
        if direction == "down":

            for block in self.blocks:
                x = block.x
                y = block.y
                block.x = x_center - (y - y_center)
                block.y = y_center + (x - x_center)

    def move(self, direction):
        for sq in self.blocks:
            sq.move(direction, 3)


class square(shape):
    def __init__(self, x, y, color):
        self.hight = 20
        self.width = 20
        self.x = x
        self.y = y
        self.color = color

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def move(self, direction, movement_speed):
        if direction == "left":
            self.x -= 21
        if direction == "right":
            self.x += 21
        if direction == "up":
            self.y -= 21
        if direction == "down":
            self.y += 21

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


class line(shape):
    def __init__(self, color, movement_speed, x, y, size):
        blocks = []
        for _ in range(size):
            blocks.append(square(x, y, color))
            x += 21
        super().__init__(color, movement_speed, blocks)


class pluse(shape):
    def __init__(self, color, movement_speed, x, y, size=4):
        size = 4
        blocks = []
        for _ in range(size - 1):
            blocks.append(square(x, y + 21, color))
            x += 21
        blocks.append(square(blocks[1].x, y, color))
        super().__init__(color, movement_speed, blocks)


class cube(shape):
    def __init__(self, color, movement_speed, x, y, size=4):
        size = 4
        blocks = []

        for _ in range(int(math.sqrt(size))):
            for __ in range(int(math.sqrt(size))):
                blocks.append(square(x + (__+1) * 21, y + 21*(_+1), color))


        super().__init__(color, movement_speed, blocks)
