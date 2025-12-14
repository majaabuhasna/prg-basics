import csv

file_name = 'clothing.csv'

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if float(row['Price']) < 60 and int(row['Stock_Quantity']) < 40:
                product_id = row['Product_ID']
                product_name = row['Product_Name']
                size = row['Size']

                print(f'{product_id}, {product_name}, {size} ')


except FileNotFoundError:
    print('File not found')