text = input('Enter a string: ')

if len(text) >= 5:
    if text[-3:] == 'ing':
        text += 'ly'
    else:
        text += 'ing'
print(text)
