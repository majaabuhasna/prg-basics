def f(expression):
    result = int(expression[0])

    for i in range(1, len(expression), 2):
        operator = expression[i]
        next_number = int(expression[i+1])

        if operator == '+':
            result += next_number
        elif operator == '-':
            result -= next_number

    return result

print(f("2+3"), f("3+8+1"), f("2+3-4+5-0"), sep='\n')