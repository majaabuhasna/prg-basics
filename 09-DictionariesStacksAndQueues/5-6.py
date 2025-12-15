basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

person = {}

person.update(basic_data)
person.update(advanced_data)

print('PERSON DATA')
print('===========')
for key, value in person.items():
    if isinstance(value, list):
        clean_value = ", ".join(value)
        print(f'{key}: {clean_value}')
    else:
        print(f'{key}: {value}')