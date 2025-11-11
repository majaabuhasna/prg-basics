age = int(input('Enter your age: '))

if age >= 65:
    print('Age group: Senior')
elif age >= 20:
    print('Age group: Adult')
elif age >= 13:
    print('Age group: Teen')
else:
    print('Age group: Child')