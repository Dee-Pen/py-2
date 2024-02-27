# Write a Python program to create a function for factorial value
def display_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

n = int(input("Enter the number to find factorial: "))

display_fact(n)