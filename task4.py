#! python3
import math
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

height = int (input("what is the height of the cone ? \n"))
radius = int (input("what is the radius of the cone ? \n"))
sh = math.sqrt(pow(height,2) + pow(radius,2))

surface_area = math.pi*radius*sh + math.pi*(pow(radius, 2))
print(f"the surface area of the cone is {surface_area}")

