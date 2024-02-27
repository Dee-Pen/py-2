# wap in py to read 5 prices and find the sum and average of all the prices

prices = []

n = int(input("Enter the number of prices: "))

for i in range(0, n):
    prices.append(int(input("Enter price: ")))

print("Original array: ", prices)

sum = 0

for i in prices:
    sum += i

print("Sum of all prices: ", sum)
print("Average of all prices: ", sum/n)

