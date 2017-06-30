# Enter the day
day = int(input('Enter Monday - 1, Tuesday - 2, ... Sunmday - 7 '))

# get the number of tickers, and membership
adult = int(input('Number of adult tickets : '))
child = int(input('Number of child tickets : '))
elder = int(input('Number of elder tickets : '))
if day < 6 :
    member = (input('Type of membership (corporate, family, none) : '))

# ticket price for weekend for all categories
weekend_ticket = 10

# ticket price for weekday
adult_ticket = 10
child_ticket = 7.5
elder_ticket = 5.5

if day < 6 :
    adult_price = adult_ticket * adult
    child_price = child_ticket * child
    elder_price = elder_ticket * elder
    if member == 'corporate' :
        total_price = adult_price + elder_price + child_price
        discount = 0.2 * total_price
        discounted_price = total_price - discount
    elif member == 'family' :
        total_price = adult_price + elder_price + child_price
        discount = child_price
        child_price = 0
        discounted_price = total_price - discount
    elif member == 'none':
        total_price = adult_price + elder_price + child_price
        discount = 0
        discounted_price = total_price
else :
    adult_price = weekend_ticket * adult
    child_price = weekend_ticket * child
    elder_price = weekend_ticket * elder
    discount = 0
    discounted_price = adult_price + child_price + elder_price


print('%d adult ticket for $%.2f' % (adult, adult_price))
print('%d child ticket for $%.2f' % (child, child_price))
print('%d elder ticket for $%.2f' % (elder, elder_price))
print('Discount = $%.2f and Total = $%.2f' % (discount, discounted_price))
