N = int(input('Enter value of N: '))

print(f'Prime numbers up to {N}...')
for number in range(2, N+1):
    sqrt = int(number ** 0.5) + 1
    for denominator in range(2, sqrt):
        if number  % denominator == 0:
            break
    else:
        print(number, end=' ')
