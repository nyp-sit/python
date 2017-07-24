print("Welcome to ABC Department Store")
print('-- Self Checkout Kiosk --')

listPrice = float(input('Enter List Price $'))

if listPrice <30:
    discountPrice = listPrice *0.5
    print('Discounted Price $%.2f @50 percent' %discountPrice)
elif 30<= listPrice <=100:
    discountPrice = listPrice - (listPrice *0.3)
    print('Discounted Price $%.2f @30 percent' %discountPrice)
else:
    discountPrice = listPrice - (listPrice *0.15)
    print('Discounted Price $%.2f @15 percent' %discountPrice)
