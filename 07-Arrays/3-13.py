def occurs(number, array):
    if number in array:
        return True
    return False


arr = [15, 38, 7, 23, 14]
number_input = int(input('Number: '))
result = occurs(number_input,arr)

print('Array: ',end='')
print(*arr)

if result == True:
    print(f'Number {number_input} appears in the array')
else:
    print(f'Number {number_input} does not appear in the array')