
try:
    with open('it_company.csv', 'r') as file:
        i = 0
        
        for line in file:
            print(line, end='')
            i += 1

            if i == 5:
                input('Press Enter key...')
                i = 0

except FileNotFoundError:
    print('File not found')