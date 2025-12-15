def hotel_list(hotels):
    names = []

    for hotel in hotels:
        names.append(hotel['name'])

    return names

def avg_price(hotels):
    total_sum = 0

    for hotel in hotels:
        total_sum += hotel['price']

    return total_sum/len(hotels)

hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

krakow_hotels = hotel_list(hotels_in_Krakow)
sopot_hotels = hotel_list(hotels_in_Sopot)

print('Hotels in Krakow:', ', '.join(krakow_hotels))
print('Average hotel price in Krakow:', avg_price(hotels_in_Krakow))

print('Hotels in Sopot:', ', '.join(sopot_hotels))
print('Average hotel price in Sopot:', avg_price(hotels_in_Sopot))

if avg_price(hotels_in_Krakow) < avg_price(hotels_in_Sopot):
    print ('Cheaper hotels in: Krakow')
else:
    print('Cheaper hotels in: Sopot')