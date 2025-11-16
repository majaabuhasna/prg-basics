def how_many_letters(text):
    amount = 0
    for letter in text:
        if letter == 'e':
            amount += 1
    return amount