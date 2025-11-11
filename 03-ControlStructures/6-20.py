decimal = int(input('Enter decimal number: '))
original_decimal = decimal

binary = ''

if decimal == 0:
    binary == '0'
else:
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

print(f'{original_decimal}(10) = {binary}(2)')