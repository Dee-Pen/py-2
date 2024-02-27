# 10.Write a program to check armstrong number.

num = int(input("Enter a number: "))
temp = num
sum = 0

while num > 0:
    rem = num % 10
    sum = sum + rem ** 3
    num = num // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not an armstrong number")

