amount = int(input('Enter the amount in PLN: '))
original_amount = amount

five_zl = 0
two_zl = 0
one_zl = 0

while amount >= 5:
    five_zl = amount // 5
    amount = amount % 5

print(f'5 PLN coins: {five_zl}')

while amount >= 2:
    two_zl = amount // 2
    amount = amount % 2

print(f'2 PLN coins: {two_zl}')

while amount >= 1:
    one_zl = amount // 1
    amount = amount % 1

print(f'1 PLN coins: {one_zl}')