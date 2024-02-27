# 20. WAP to find the Roots of a Quadratic Equation
# Example: ax^2 + bx + c = 0
# 2x^2 + 5x + 3 = 0

import math # if you dont want to use math.sqrt(), use d**0.5

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b**2 - 4*a*c

if d > 0:
    print("Roots are real and unequal")
    print("Root 1: ",(-b + math.sqrt(d))/(2*a))
    print("Root 2: ",(-b - math.sqrt(d))/(2*a))
elif d == 0:
    print("Roots are real and equal")
    print("Root 1: ",(-b + math.sqrt(d))/(2*a))
    print("Root 2: ",(-b - math.sqrt(d))/(2*a))
else:
    print("Roots are imaginary")
    print("Root 1: ",(-b + math.sqrt(d))/(2*a))
    print("Root 2: ",(-b - math.sqrt(d))/(2*a))

