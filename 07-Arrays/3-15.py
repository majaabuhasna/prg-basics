my_tuple = (10,20,30,40,50)
reversed_tuple = my_tuple[::-1]

print('Tuple: ',end='')
print(*my_tuple,sep=', ')
print('Reverse order: ',end='')
print(*reversed_tuple,sep=', ')