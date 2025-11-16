def f(n):
    n = int(n)
    i = 0
    j = 1

    if n == 1:
        return print(0)
    
    if n == 2:
        return print(1)

    for n in range(n-2):
        k = i + j
        i = j
        j = k
    
    return print(k)

f(5)
f(9)

        