stack = []

expression = {}

while True:
    value = input('Enter any number, an operator (+ - * / ) or the equal sign (=): ').strip()

    if value == '=':
        if len(stack)>0:
            print(f'Result: {int(stack.pop())}')
        else:
            print('No result')
        break

    elif value == '+' or value == '-' or value == '*' or value == '/':
        if len(stack)<2:
            print('Not enough numbers in stack to continue')
            continue

        item1 = stack.pop()
        item2 = stack.pop()

        result = 0
        if value == '+':
            result = item2 + item1
        elif value == '-':
            result = item2 - item1
        elif value == '*':
            result = item2 * item1
        elif value == '/':
            if item1 == 0:
                print('Cannot divide by 0')
                stack.append(item2)
                stack.append(item1)
                continue
            result = item2 / item1

        stack.append(result)
    
    else:
        try:
            number = float(value)
            stack.append(number)
        except ValueError:
            print('Unknown command')