age = int(input("Enter age: "))

if age>=4 and age <=130:
    day = int(input("Enter day of week (1-Mon, 2-Tues... 7-Sun): "))
    if day == 6 or day == 7:
        price = 10
    else:
        if age <16:
            price = 7.5
        elif age < 65:
            price = 10
        else:
            price = 5.5
    print("You have to pay $%.2f for the ticket." % (price))
else:
    print("Invalid age. Must be between 4 and 130.")
