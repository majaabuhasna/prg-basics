# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

product_values = []

for i in range(len(product_prices)):
    product_values.append(product_prices[i]*product_quantities[i])

value_of_all_goods = 0
for value in product_values:
    value_of_all_goods += value

print(f'The value of all the goods available in the store is {value_of_all_goods:.2f}')