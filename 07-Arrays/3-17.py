my_tuple = (50,20,40,50,30,50)
print('Tuple: ',end='')
print(*my_tuple, sep=',')

value = input('Value: ')


occurences = 0
for i in my_tuple:
    if i == int(value):
        occurences += 1

print(f'Number of occurrences: {occurences}')