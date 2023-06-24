# Python program to find the area of a triangle
import math
a=float(input("Enter first side of a triangle:"))
b=float(input("Enter second side of a triangle:"))
c=float(input("Enter third side of a triangle:"))
s=(a+b+c)/2
area=round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)
print("Area of a triangle is:",area)