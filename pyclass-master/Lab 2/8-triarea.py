# Write a Python program to accept 3 sides of triangle and find the area of
# triangle

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("Area of triangle is: ", area)