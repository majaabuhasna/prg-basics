###
# Functions to read any data type from the keyboard
#
def input_string(message):
    string_inp = str(input(message))
    return string_inp

def input_integer(message):
    integer_inp = int(input(message))
    return integer_inp

def input_real(message):
    real_inp = float(input(message))
    return real_inp

def input_boolean(message):
    boolean_inp = bool(input(message))
    return boolean_inp