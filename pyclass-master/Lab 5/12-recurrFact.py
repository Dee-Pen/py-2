#wap to find factorial of a number using recursion

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
    
num = int(input("Enter a number: "))
print("Factorial: ", fact(num))

