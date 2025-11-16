def f(x,y):
    i = 0
    if x < 0 and y > 0:
        i = abs(x) // 2

        return i

    if x < 0 and y < 0:
        i = (x - y) // 2
        i = abs(i)

        return i

    
print(f(-7,8))
print(f(-1,11))
            

