def f(n):
    n = int(n)
    i = 0
    j = 1

    if n == 1:
        return 0
    
    if n == 2:
        return 1

    for n in range(n-2):
        k = i + j
        i = j
        j = k
    
    return k

print(f(5), f(9), sep="\n")

        