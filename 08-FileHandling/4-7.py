import re

text = input('Enter text: ')

pattern = '[aeiouy]'

vowels = 0

for char in text:
    match = re.match(pattern,char,re.IGNORECASE)
    if match:
        vowels += 1

print(f'Vowels in text: {vowels}')