def is_number(string):
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True

def is_valid_phone(string):
    if len(string) == 8:
        if string[0] == '6' or string[0] == '9':
            return True
    return False

