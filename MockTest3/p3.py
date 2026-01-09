def f(d):
    number = 0
    sum_passengers = 0
    for key,value in d.items():
        sum_passengers += value

    average = sum_passengers / len(d)

    for value in d.values():
        if value > average:
            number += 1
        
    return number

print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))
    