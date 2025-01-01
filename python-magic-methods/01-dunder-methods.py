# Dunder / Magic methods
# Dunder stands for double underscore
# These are special / reserved methods in Python that map to some kind of behaviour
# __init__ is used to construct or create a new object

from math import sqrt
class Rect:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y)

rectangle = Rect(3, 4)
print("The absolute value of the diagonal of the rectangle is", abs(rectangle), sep=": ", flush=True)
