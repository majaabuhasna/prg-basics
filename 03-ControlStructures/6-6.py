hours = int(input('Enter the number of hours the car was parked: '))
cost = 0

if hours > 6:
    cost = 20
elif hours >= 3:
    cost = 15
elif hours >= 1:
    cost = 5

print(f'You must pay {cost} PLN')