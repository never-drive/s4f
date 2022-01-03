class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    @classmethod
    def zero(cls):
        return cls(0, 0)

    # https://rszalski.github.io/magicmethods/
    def __str__(self) -> str:
        return f"Point ({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
point.draw()

Point.zero().draw()    # static method
print(point)           # made use of __str__

other = Point(1, 2)
print(point == other)  # made use of __eq__
print(point > other)   # made use of __gt__

combined = point + other
print(combined)        # made use of __add__
