# wap to display multiplication table of a given number

num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

    