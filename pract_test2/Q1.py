count = int(input('No of expense records you want to enter: '))

sum = 0
for i in range(count):
    amount = float(input('Please enter the expenses amount: '))
    sum += amount

print('Total expenses you have entered is $%.2f' %sum)

