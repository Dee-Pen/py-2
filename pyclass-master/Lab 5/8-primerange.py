# wap to display prime numbers from a given range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

            