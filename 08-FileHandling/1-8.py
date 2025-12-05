with open('pets.txt', 'r') as file:
    content = file.read()

text_split = content.splitlines()

total_words = 0

for line in text_split:
    words_in_line = line.split()
    total_words += len(words_in_line)

print(total_words)