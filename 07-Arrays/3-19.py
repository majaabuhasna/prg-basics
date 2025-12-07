arr = [3.12,5,9.4,2.5,1,7.48]
print(f'Array: {arr}')

value = float(input('Enter value: '))

amount = 0

for digit in arr:
    if digit > value:
        amount += 1

print(f'Number of elements that are greater than the given value: {amount}')


