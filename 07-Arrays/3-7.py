arr = ['Genowefa','Onufry','Celestyna','Alojzy','Pankracy']

names = ' '.join(arr)
print(f'Names: {names}')

longest_name = ''
for name in arr:
    if len(name) > len(longest_name):
        longest_name = name

print(f'Longest name: {longest_name}')