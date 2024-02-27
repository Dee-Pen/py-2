# Write program to find the sum of factorial upto n terms


num = int(input("Enter the number to find factorial: "))

fact = 1
sum = 0
for i in range(1, num+1):
    fact = fact * i
    sum = sum + fact
print("The sum of factorial upto", num, "terms is", sum)