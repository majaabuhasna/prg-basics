arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),("Jackson","Peter"),("Johnson","Rick"),("Lewis","Terry"),("Clarke","Robin")]

result = list(map(lambda data: f'{data[0].upper()}, {data[1]}',arr))

for item in result:
    print(item)