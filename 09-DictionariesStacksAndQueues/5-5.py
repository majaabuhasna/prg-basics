paragraph = "cat dog mouse cat rat cat mouse"
words = paragraph.split()


dictionary = {}

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

for key,value in dictionary.items():
    if value == 1:
        print(f'The word "{key}" has appeared {value} time in the paragraph')
    else:
        print(f'The word "{key}" has appeared {value} times in the paragraph')
    