# WAP that repeatedly asks the user to enter product names and prices. Store all of them in a
# dictionary whose keys are product names and values are prices. And also write a code to search
# an item from the dictionary.



productDict = {}


while True:
    productName = input("Enter the product name: or done to exit:")
    if productName == "done":
        break
    productPrice = input("Enter the product price: ")
    productDict[productName] = productPrice
    print(productDict)
    searchItem = input("Enter the product name to search: ")
    if searchItem in productDict:
        print("The price of the product is: ", productDict[searchItem])
    else:
        print("The product is not in the list")

