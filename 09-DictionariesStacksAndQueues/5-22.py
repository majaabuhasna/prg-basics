import json

name = str(input('Enter name of product: '))
price = float(input('Enter price of product (with two decimal places): '))
paid = bool(input('Paid (True/False): '))

data = {
    'name' : name,
    'price' : price,
    'paid' : paid
}

file_name = 'product.json'

with open(file_name,'a',encoding='utf-8') as file:
    json.dump(data,file,indent=4)

print('The product has been successfully saved in the product.json file!')