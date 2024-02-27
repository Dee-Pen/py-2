# Write a program to create a nested tuple to store roll number, name and marks of students.


studentTuple = ()
while True:
    roll = input("Enter the roll number: or done to exit:")
    if roll == "done":
        break
    name = input("Enter the student name: ")
    marks = input("Enter the student marks: ")
    studentTuple = studentTuple + ((roll, name, marks),)
print(studentTuple)
