def isPalin():
    num = int(input("Please enter a number: "))
    backnum = num

    rev = 0

    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10

    if backnum == rev:
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!") 

isPalin()