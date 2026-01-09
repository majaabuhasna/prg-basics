def f(fnc,res):
    arr = []
    for i in res:
        if fnc(i):
            arr.append(i)

    maximum_nr = max(arr)
    minimum_nr = min(arr)

    difference = maximum_nr - minimum_nr

    return difference

res1 = [95,90,20,50,70]
fnc1 = lambda x: x>50
fnc2 = lambda x: x>30 and x<90

print(f(fnc1,res1))
print(f(fnc2,res1))