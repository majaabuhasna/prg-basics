def f(n):
    n = n * 2 - 1
    for m in range(0,n):
        if m % 2 == 0:
            print('*', end='')
        else:
            print('/', end='')
    return m

f(4)
print()
f(1)