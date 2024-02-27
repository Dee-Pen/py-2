# wap in py to accept an array of numbers and delete even numbers and print the array

array = []

n = int(input("Enter the number of elements in the array: "))

for i in range(0, n):
    array.append(int(input("Enter element: ")))

print("Original array: ", array)

for i in array:
    if i % 2 == 0:
        array.remove(i)

print("Array after deleting even numbers: ", array)


