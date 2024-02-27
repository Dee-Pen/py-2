s1 = float(input("Please Enter Marks in 1st Subject: "))
s2 = float(input("Please Enter Marks in 2st Subject: "))
s3 = float(input("Please Enter Marks in 3st Subject: "))

avg = (s1+s2+s3)/3

if (avg>=90 and avg <=100):
    print("Grade A")
elif(avg>=80 and avg <=89):
    print("Grade B")
elif(avg>=70 and avg <=79):
    print("Grade C")
elif(avg>=60 and avg <=69):
    print("Grade D")
elif(avg>=0 and avg <=59):
    print("Grade F")
else:
    print("Invalid Marks")