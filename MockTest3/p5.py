def f(mnumbers):
    import re
    pattern = '^[+-]?[1-7a-dA-D]+$'

    total = 0

    for number in mnumbers:
        if re.match(pattern,number):
            total += 1

    return total

print(f(["A15","-31","7abC","+D1","-g4"]))
print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"]))
