# Write a program to swap two values using tuple assignment

myTuple = (1, 2)
print(myTuple)
a, b = myTuple
a, b = b, a
myTuple = (a, b)
print(myTuple)