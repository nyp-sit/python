text = input('Enter a string: ')

upperCount = 0

for char in text:
    if char.isupper():
        upperCount +=1

if upperCount >=2:
    print(text.upper())
else:
    print("The string contains less than 2 uppercase characters")
