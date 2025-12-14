price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print('Products before discount:')
for key,value in price_list.items():
    print(f'{key}: {value}')

total_before_discount = sum(price_list.values())
print()
print(f'Total before discount: {total_before_discount}')

print()

for key in price_list:
    price_list[key] = round(price_list[key] * 0.9, 2)

print('Products after discount:')
for key,value in price_list.items():
    print(f'{key}: {value}')

total_after_discount = sum(price_list.values())
print()
print(f'Total before discount: {total_after_discount}')