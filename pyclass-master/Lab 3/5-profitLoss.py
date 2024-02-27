# . WAP that input cost price(cp) and selling price (sp) and determine whether there is profit or loss.

cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))

if cp > sp:
    print("There is loss")
elif sp > cp:
    print("There is profit")
else:
    print("No profit no loss")