###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = float(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consuption in liters per 100 km: '))
total_fuel_consumption = distance*fuel_consumption/100
total_cost = fuel_consumption*fuel_price
print(f'Total fuel consuption for {distance} km:{total_fuel_consumption: .2f}')
print(f'Total cost is for {distance} km:{total_cost: .2f}')