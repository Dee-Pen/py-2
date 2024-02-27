age = int(input("Enter your age:"))

if (age>0 and age <13):
    print("Child")
elif(age>12 and age<20):
    print("Teenager")
elif(age>19 and age<60):
    print("Adult")
else:
    print("Senior Citizens")