#Author: Bernardo Calvo

MAX_SIZE = 50
MSG_TOOBIG = "Too big for picture."
MSG_RECT = "Rectangle(width={}, height={})"
MSG_SQUARE = "Square(side={})"

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > MAX_SIZE or self.height > MAX_SIZE:
      return MSG_TOOBIG
    txt = ""
    for i in range(self.height):
      txt += "".ljust(self.width, '*') + '\n'
    return txt

  def get_amount_inside(self, oshape):
    return int(self.width/oshape.width) * int(self.height/oshape.height)

  def __str__(self):
    return MSG_RECT.format(self.width, self.height)

class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)

  def set_side(self, length):
    super().set_width(length)
    super().set_height(length)

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)

  def __str__(self):
    return MSG_SQUARE.format(self.width)

#Example
rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
