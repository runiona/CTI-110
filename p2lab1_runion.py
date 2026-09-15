"""
CTI 110
P2LAB1
runiona
9/15/26
Get Radius, calculate and display radius, circumference, and area
"""

PI = 3.14159
# input -- get radius
radius =float(input("what is the radius of the circle? "))

#calculation -- find diameter, circumference, and area
# diameter = 2*r, circumference = 2*pi*r, area= pi*r*r
diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius

#Output -- .1f, .2f, 3.f
print(f"The diameter is {diameter:.1f}.")
print(f"The circumference is {circumference:.2f}")
print(f"The area is {area:.3f}")