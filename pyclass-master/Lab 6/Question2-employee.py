# Write a Python program to enter names of employees and their salaries as input and store
# them in a dictionary


employeeDict = {}

while True:
    employeeName = input("Enter the employee name: or done to exit:")
    if employeeName == "done":
        break
    employeeSalary = input("Enter the employee salary: ")
    employeeDict[employeeName] = employeeSalary
    print(employeeDict)
    