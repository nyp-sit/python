# input() function will prompt the users to enter some value
# The value assigned is always a String value
# Before you can perform arithmetic operation, convert to either a float (decimal) or integer using
# float() or int() function

celsius = float(input('Enter the temperature in celsius: '))
fahrenheit = 9/5 *celsius + 32
print("The temperature in Fahrenheit is ",fahrenheit)
