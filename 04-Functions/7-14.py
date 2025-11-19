def f(number1,number2,operator):
    if operator == '+':
        result = number1 + number2
        return result
    elif operator == '-':
        result = number1 - number2
        return result
    elif operator == '*':
        result = number1 * number2
        return result
    elif operator == '%':
        result = number1 % number2
        return result
    elif operator == "**":
        result = number1 ** number2
        return result
    else:
        return 'Incorrect sign'


print(f(2,3, "+"), f(2,3, "%"), f(2,3, "**"), f(2,3, "*"), f(2,3, "-"), sep="\n")