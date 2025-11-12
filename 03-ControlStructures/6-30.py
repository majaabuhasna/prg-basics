for row in range(1,8):
    for column in range(0,7):
        number = row + (column*7)
        print(f'{number}', end=' ')
    print()