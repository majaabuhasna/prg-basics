stock = [(20, 5.50), (15, 8.30), (37, 3.85), (4, 11.60)]

total_value = sum(map(lambda x: x[0] * x[1], stock))

print("Products in stock:", stock)
print("Total value:", round(total_value, 2))