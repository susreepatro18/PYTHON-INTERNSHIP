import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_circumference(self):
        return self.get_perimeter()

# Main code for testing
if __name__ == "__main__":
    # Create a new Circle object
    circle = Circle(0, 0, 5)

    # Display the area of the circle
    print("Area of the circle:", circle.get_area())

    # Display the perimeter of the circle
    print("Perimeter of the circle:", circle.get_perimeter())

    # Display the circumference of the circle
    print("Circumference of the circle:", circle.get_circumference())
