import math

class Circle:
    """A class to facilitate working with circles"""
    def __init__(self, r):
        try:
            self.radius = r if r > 0 else print('Please provide a positive number.')
        except TypeError: 
            print("Please provide a number.")

    def __str__(self):
        return f"Circle of radius {self.radius}"

    def circumference(self):
        """Returns the circumference of the circle"""
        return round(2*math.pi*self.radius, 2)

    def area(self):
        """Returns the area of the circle"""
        return round(math.pi*(self.radius**2), 2)

    def __eq__(self, other):
        return self.radius == other.radius
        
    def __ne__(self, other):
        return self.radius != other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius


# Inspect the documentation
print(Circle.__doc__) # Output: A class to facilitate working with circles
print(Circle.circumference.__doc__) # Output: Returns the circumference of the circle
print(Circle.area.__doc__) # Output: Returns the area of the circle

# Create some Circle objects
circle_1 = Circle(4)
circle_2 = Circle(5.3)
circle_3 = Circle(-2) # Output: an appropriate error message
circle_4 = Circle('a') # Output: an appropriate error message

# Print them
print(circle_1) # Output: Circle of radius 4
print(circle_2) # Output: Circle of radius 5.3

# Get their circumference and area
print(circle_1.circumference()) # Output: 25.13
print(circle_1.area()) # Output: 50.27
print(circle_2.circumference()) # Output: 33.3
print(circle_2.area()) # Output: 88.25

# Compare them
print(circle_1 < circle_2) # Output: True
print(circle_1 <= circle_2) # Output: True
print(circle_1 == circle_2) # Output: False
print(circle_1 >= circle_2) # Output: False
print(circle_1 > circle_2) # Output: False