# Conditional decision and repetitive loop will be covered later
# This is just a reference solution, and we will revisit this solution again in future

while True :
    celsius = input('Enter the temperature in celsius: ')
    if celsius.isdecimal() :
        c = float(celsius)
        fahrenheit = 9/5 * c + 32
        print("The temperature in Fahrenheit is ",fahrenheit)
    else :
        break
