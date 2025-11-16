def f(number1,number2,operator):
    if operator == '+':
        result = number1 + number2
        return print(result)
    elif operator == '-':
        result = number1 - number2
        return print(result)
    elif operator == '*':
        result = number1 * number2
        return print(result)
    elif operator == '%':
        result = number1 % number2
        return print(result)
    elif operator == "**":
        result = number1 ** number2
        return print(result)
    else:
        return print('Incorrect sign')


f(2,3, "+")
f(2,3, "%")
f(2,3, "**")
f(2,3, "*")
f(2,3, "-")