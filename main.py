** start of main.py **

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        row = "*" * self.width
        picture = "\n".join([row for _ in range(self.height)])
        return picture + "\n"   # trailing newline fixes the test

    def get_amount_inside(self, other):
        return (self.width // other.width) * (self.height // other.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_side(self, value):
        self.width = value
        self.height = value

    def set_width(self, value):
        self.set_side(value)

    def set_height(self, value):
        self.set_side(value)

** end of main.py **

