# wap to create a child class teacher that will inherit properties from parent class staff

class Staff:
    Department = "IT"

class Teachers(Staff):
    pass

print(Teachers.Department)