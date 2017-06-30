height = float(input("Enter your height in m: "))

lower_weight = 18.5 * height ** 2
higher_weight = 22.9 * height ** 2

print('Your ideal weight is between %.1f and %.1f' % (lower_weight, higher_weight))
