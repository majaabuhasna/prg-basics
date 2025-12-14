file_name = input('Enter file name: ')

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

        lines = content.splitlines()
        number_of_lines = len(lines)

        words = content.split()
        number_of_words = len(words)

        number_of_characters = len(content)

        print(f'Number of lines: {number_of_lines}')
        print(f'Number of words: {number_of_words}')
        print(f'Number of characters: {number_of_characters}')

except FileNotFoundError:
    print('Sorry! This file does not exist')