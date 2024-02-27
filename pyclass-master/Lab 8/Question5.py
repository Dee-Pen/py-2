#calculate area of different shapes using method overridding and ineritance

class Shape:
    def __init__(self):
        self.len = 0
        self.bre = 0
        self.hei = 0

class Square(Shape):
    def __init__(self,len):
        self.len = len

    def area(self):
        return self.len**2
    
class Rectangle(Shape):
    def __init__(self,len,bre):
        self.len = len
        self.bre = bre

    def area(self):
        return self.len*self.bre


length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
height = float(input("Enter the height: "))

s = Square(length)
r = Rectangle(length,breadth)

print("Area of square: ",s.area())
print("Area of rectangle: ",r.area())

