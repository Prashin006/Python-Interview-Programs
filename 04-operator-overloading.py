class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError("Unsupported operand type!")

    def __str__(self):
        return f"Point ({self.x}, {self.y})"


p1 = Point(3, 4)
p2 = Point(5, 6)

print(p1.add(p2))
print(p1.add(2))
print(p1.add("Prashin"))
