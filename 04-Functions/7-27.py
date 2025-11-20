def f(product_code):
    
    if len(product_code) != 4:
        return 'Product code must be 4 digits'
    else:
        control_digit = int(product_code[-1])

    sum = 0
    for digit in product_code[0:3]:
        digit = int(digit)
        sum += digit

    if sum % 7 == control_digit:
        return True
    
    return False

print(f("1082"), f("2035"), f("1114"), f("7071"), sep='\n')

