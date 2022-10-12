# Program Name: Area of Circle
# Name: Ysmael R. Trias Jr
# Program Details: Calculate the area of circle
# Date Created: October 12, 2022

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circle_area (self):
        return math.pi*(self.radius**2)

x = int(input(" Enter the radius of the circle: "))
val = Circle(x)

print (" The area of the circle is: ", val.circle_area())
