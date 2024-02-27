# Write a program that prompts the user to enter number in two variables and
# swap the contents of the variables

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Before swapping: ")
print("a = ", a)
print("b = ", b)

temp = a
a = b
b = temp

print("After swapping: ")
print("a = ", a)
print("b = ", b)

