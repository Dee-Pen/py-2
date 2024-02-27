wt = float(input("Enter Weight in KG: "))
ht = float(input("Enter Height in Meters: "))

bmi = wt /(ht**2)

print("BMI: ",bmi)

if bmi<18.5:
    print("Underweight")
elif(bmi>=18.5 and bmi<=24.9):
    print("Normal Weight")
elif(bmi>=25 and bmi<=29.9):
    print("Overweight")
elif(bmi>=30):
    print("Obesity")
else:
    print("Unclear")

    

