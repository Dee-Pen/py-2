# Write a Python program that create a tuple storing first 9 terms of Fibonacci series


a= 0
b= 1
c= 0
fibotuple= (a, b)
for i in range(7):
    c= a+b
    a= b
    b= c
    fibotuple= fibotuple + (c,)
print(fibotuple)
    