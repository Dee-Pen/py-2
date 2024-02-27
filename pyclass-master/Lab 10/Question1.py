# wap to create a class by name,student,and initialize attributes like name age and grade while creating and object

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade



student1=Student("Ram",20,"A+")
student2=Student("Laxman",18,"A")

print("Student 1:")
print("Name: ", student1.name)
print("Age: ",student1.age)
print("Grade: ",student1.grade)

print("\nStudent 2:")
print("Name: ", student2.name)
print("Age: ",student2.age)
print("Grade: ",student2.grade)