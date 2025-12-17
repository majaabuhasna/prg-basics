import json

with open('euro.json','r',encoding='utf-8') as file:
    data = json.load(file)

print(f'{'Date':<15} {'Buying rate':<15} {'Selling rate':<15}')
print('=' * 45)

rates_list = data['rates']

for rate in rates_list:
    date = rate['effectiveDate']
    buying_rate = rate['bid']
    selling_rate = rate['ask']

    print(f'{date:<15} {buying_rate:<15} {selling_rate:<15}')