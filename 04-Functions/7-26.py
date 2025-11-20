def f(text):
    separated_text = ''

    if text == '':
        return text

    for char in text[:-1:]:
        separated_text += char + '-'
    for char in text[-1]:
        separated_text += char

    return separated_text

print(f("Univesity"), f("UE"), f("x"), f(""), sep='\n')