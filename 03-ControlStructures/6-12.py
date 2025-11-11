product_amount = int(input("Number of products purchased: "))
product_price = int(input("Product price: "))
amount_to_pay = 0

if product_amount > 0 and product_price > 0:
    if product_amount <= 2:
        amount_to_pay = product_amount * product_price

    else:
        amount_to_pay = product_price * 2 + (product_amount - 2) * product_price * 0.75

    print(f"Amount to pay: {amount_to_pay}")

else:
    print("Invalid number.")
