# Write a program that prompts the user to input the length and the
# width of a rectangle and outputs the area and perimeter of the
# rectangle.

l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))

area = l * b
perimeter = 2 * (l + b)

print("Area of rectangle: ", area)
print("Perimeter of rectangle: ", perimeter)

