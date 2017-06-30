age = int(input("Enter age: "))
if age <16:
    price = 7.5
elif age < 65:
    price = 10
else:
    price = 5.5
print("You have to pay $%.2f for the ticket." % (price))
