
import currency as cy

original = input('Enter the currency to convert from (SGD) : ')
to = input('Enter the currency to convert to (USD, JPY, EUR) : ')
amount = float(input('Enter the amount to be converted : '))

amt = cy.convert(original, to, amount)
if amt == -1:
    print('We are not able to convert from', original, 'to', to)
else:
    print(amount, 'SGD is', amt, to)
