# 7. Write a program to check prime number.

num = int(input("Enter a number: "))
flag = 0
for i in range(2,num):
    if num % i == 0:
        flag = 1
        break
if flag == 0:
    print("Prime number")
else:
    print("Not a prime number")
    