current_product_price = int(input('Current product price: '))
previous_product_price = int(input('Previous product price: '))

print(f"Current product price: {current_product_price}")
print(f"Previous product price: {previous_product_price}")

reduction = 1 - (current_product_price / previous_product_price)

if reduction >= 0.1:
    print("Buy the product!!")
    print(f"Product price reduced by {reduction:.0%}")

else:
    print(f"Product price reduced by {reduction:.0%}")