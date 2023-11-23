class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, value):
        self.x = value

    def get_y(self):
        return self.y

    def set_y(self, value):
        self.y = value

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Class for testing
class TestPoint:
    def test(self):
        point1 = Point(5,7)
        point2 = Point(8,6)

        print(f"Default point coordinates: ({point1.get_x()}, {point1.get_y()})")
        print(f"Point2 coordinates: ({point2.get_x()}, {point2.get_y()})")
        print(f"Distance between default point and Point2: {point1.distance(point2)}")
        print(f"Norm of Point2: {point2.norm()}")

# Create an instance of TestPoint and execute the test
test_point = TestPoint()
test_point.test()
