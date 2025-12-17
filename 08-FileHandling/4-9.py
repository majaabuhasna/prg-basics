import csv

file_name = 'it_company.csv'

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        print('GRAPHIC DESIGNERS')
        print('=================')


        for row in reader:
            if row['Job Title'] == 'Graphic Designer':

                first_name = row['First Name']
                last_name = row['Last Name']
                email = row['Email']

                print(f'{first_name} {last_name},{email}')


except FileNotFoundError:
    print('File not found')