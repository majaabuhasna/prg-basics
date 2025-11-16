def f(binary_number):
    binary_number = str(binary_number)
    for char in binary_number:
        if char != '0' and char != '1':
            return False
    return True