balance = float(input("Enter starting account balance (S$): "))
interestRate = float(input("Enter compound interest per month (%): "))
expense = float(input("Enter expense per month (S$): "))

month =0
while balance >0:
    month+=1
    interest = balance * (interestRate/100)
    if interest > expense :
        break
    balance = balance + interest - expense
    print('Balance after month %d is %f' % (month, balance))
if balance < 0 :
    print("The account will be depleted in", month, "months")
else :
    print('The account will never be depleted')
