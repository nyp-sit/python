weight = float(input("Enter package weight (g): "))
if weight <= 20:
    postage = 0.30 *weight
elif weight <=40:
    postage = 0.60 * weight
elif weight <=100:
    postage = 0.90*weight
else:
    postage = 1.15*weight
print("The postage charge is $%3.2f" % (postage))
