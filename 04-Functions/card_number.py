def hide(card_number):
    if len(card_number) != 16:
        print('Invalid number!! The credit card number consists of 16 digits')
    else:
        first_two = card_number[0:2]
        last_four = card_number[-4:]
        masked_part = '*' * 10

    return first_two + masked_part + last_four