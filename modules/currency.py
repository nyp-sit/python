

def convert(original, to, amount):
    amt = -1
    if original == 'SGD':
        if to == 'JPY':
            amt = amount * 81.61
        elif to == 'EUR':
            amt = amount * 0.63
        elif to == 'USD':
            amt = amount * 0.73
    return amt
