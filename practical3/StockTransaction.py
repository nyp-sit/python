currentPrice = float(input("Enter current price for ABC Bank Corporation (S$):"))

purchasePrice = 2000 * 0.4
buyCommission = purchasePrice * 0.03

sellPrice = 2000 * currentPrice
sellCommission = sellPrice * 0.02

totalCommission = buyCommission + sellCommission

print("You paid total commission of (S$)", totalCommission)

if sellPrice > (purchasePrice + totalCommission):
    print("You have made a profit of (S$)", (sellPrice - purchasePrice - totalCommission))
else:
    print("You have made a lost of (S$)", (-1* (sellPrice - purchasePrice - totalCommission)))
