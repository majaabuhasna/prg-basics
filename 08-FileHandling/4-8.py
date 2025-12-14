import re

try:
    with open('files.txt', 'r') as file:
        content = file.read()

    pattern = '[.]\w{4}'

    lines = content.splitlines()

    for line in lines:
        match = re.search(pattern,line)
        if match:
            print(line)

except FileNotFoundError:
    print('File not found')