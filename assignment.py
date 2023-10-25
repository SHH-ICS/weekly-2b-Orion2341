import math 
txt = "Hello, welcome to circle solver!"
radius = float(input("Enter the radius"))
circumference = 2*math.pi*radius
area = math.pi*radius**2
x = txt.center(80)
print(x)
print("Circumference =", circumference)
print("Area =", area)