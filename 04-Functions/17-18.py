def f(sentence):
    sentence = str(sentence)
    for char in sentence:
        if char == ' ':
            print('',end='')
        else:
            print(char,end='')
    return sentence

f("integrated development environment")
print()
f("A programming language is a system of notation for writing computer programs")