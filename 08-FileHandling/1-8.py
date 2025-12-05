with open('pets.txt', 'r') as file:
    content = file.read()

text_split = content.splitlines()

for line in text_split:
    length = len(line)
    print(length)