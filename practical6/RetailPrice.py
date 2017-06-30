

wholesaleCost = float(input("Enter the wholesale cost of product: $"))
while wholesaleCost > 0:
    retailPrice = wholesaleCost * 1.25
    print("The retail price is $%.2f" % (retailPrice))
    wholesaleCost = float(input("Enter the wholesale cost of product: $"))
