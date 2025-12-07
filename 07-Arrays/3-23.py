import MyText

text = 'An apple a day keeps the doctor away'

print(f'Text: {text}')
print('Number of words:',MyText.number_of_words(text))
print('Words from the longest: ',end='')
print(*MyText.words_from_longest_to_shortest(text),sep=',')
print('Words ordered alphabetically: ',end='')
print(*MyText.alphabetical_order(text),sep=',')