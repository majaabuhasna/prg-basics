import json

with open('reservations.json','r',encoding='utf-8') as file:
    data = json.load(file)

def number_of_rooms(reservations_data):
    rooms = 0
    reservations_list = reservations_data['reservations']

    for reservation in reservations_list:
        rooms += 1

    return rooms

def number_of_paid_reservations(reservations_data):
    paid = 0
    reservations_list = reservations_data['reservations']

    for reservation in reservations_list:
        if reservation['paid'] == True:
            paid += 1

    return paid

def number_of_unpaid_reservations(reservations_data):
    unpaid = 0
    reservations_list = reservations_data['reservations']

    for reservation in reservations_list:
        if reservation['paid'] == False:
            unpaid += 1

    return unpaid

def total_paid(reservations_data):
    total = 0
    reservations_list = reservations_data['reservations']

    for reservation in reservations_list:
        if reservation['paid'] == True:
            total += reservation['price_per_night'] * reservation['nights']

    return total

def total_unpaid(reservations_data):
    total = 0
    reservations_list = reservations_data['reservations']

    for reservation in reservations_list:
        if reservation['paid'] == False:
            total += reservation['price_per_night'] * reservation['nights']

    return total

print('RESERVATIONS SUMMARY')
print('=====================')
print(f'Number of rooms: {number_of_rooms(data)}')
print(f'Number of paid reservations: {number_of_paid_reservations(data)}')
print(f'Number of unpaid reservations: {number_of_unpaid_reservations(data)}')
print(f'Total value of paid reservations: {total_paid(data)}')
print(f'Total value of unpaid reservations: {total_unpaid(data)}')