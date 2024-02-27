# find area of rectangle using class and object

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
rect = Rectangle(length, width)
print("Area of rectangle: ", rect.area())
