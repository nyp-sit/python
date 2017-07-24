# visa - 4
# master - 51 to 55
# Amex - 34 to 37

while True :
    s = input('Enter your credit card number : ')
    if len(s) == 16:
        if int(s[0]) == 4:
            card = 'Visa'
            number = s[-4:]
            break
        else :
            print('You have entered an unknown 16 digit numbers')
    elif len(s) == 15:
        if int(s[0:2]) >33 and int(s[0:2]) < 38:
            card = 'Amex'
            number = s[-4:]
            break
        else :
            print('You have entered an unknown 15 digit numbers')
    else:
        print('You have entered an invalid credit card number')

print('You have a valid %s card and the last 4 digit is %s' % (card, number))
