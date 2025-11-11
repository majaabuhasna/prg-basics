pin = '0805'
attempts = 0

while attempts < 3:
    enter_pin = input('Enter PIN: ')

    if enter_pin == pin:
        print('Success.')
        break

    if enter_pin != pin:
        attempts += 1
        print('Incorrect...')

if attempts == 3:
    print('Sorry, your payment card has been blocked.')