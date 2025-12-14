try:
    file_name = 'numbers.txt'
    
    with open(file_name, 'w', encoding='utf-8') as file:
        for number in range(1,101):

            line = f'{number},{number**2},{number**3}'

            if number < 100:
                file.write(line + '\n')
            else:
                file.write(line)

except FileNotFoundError:
    print('File not found')