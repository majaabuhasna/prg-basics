price = float(input('Enter product price: '))
discount = float(input('Enter product discount %: '))

reduction = price*discount/100
price_with_discount = price - reduction

print(f'Price with discount:{price_with_discount: .2f}')
print(f'Reduction:{reduction: .2f}')