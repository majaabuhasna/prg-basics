###
# Functions to read any data type from the keyboard
#
def input_string(message):
    value = input(message)
    return str(value)

def input_integer(message):
    value = input(message)
    return int(value)

def input_real(message):
    value = input(message)
    return float(value)

def input_boolean(message):
    value = input(message)
    if value == 'y':
        return True
    if value == 'n':
        return False