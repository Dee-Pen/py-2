#4. WAP to find the greatest number among four numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print("First number is greatest")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("Second number is greatest")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("Third number is greatest")
elif num4 > num1 and num4 > num2 and num4 > num3:
    print("Fourth number is greatest")
else:
    print("All numbers are equal")