import csv

with open('vehicle.txt','r',encoding='utf-8') as vehicles:
    content = vehicles.read().split()

dictionary = {}

for line in content:
    if line[0] in dictionary:
        dictionary[line[0]] += 1
    else:
        dictionary[line[0]] = 1

print(dictionary)

with open('province.csv','r',encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        letter = row['Letter']
        province = row['Name']
        
        if letter in dictionary:
            count = dictionary[letter]
            print(f'{province}: {count}')
