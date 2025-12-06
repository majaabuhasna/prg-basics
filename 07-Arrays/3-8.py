arr = [2, 6, 4, 9, 7]

def star(n):
    return '*' * n

for number in arr:
    stars = star(number)
    print(f'{number}: {stars}')