arr = [-15, 8, -31, 47, -2, 19]

flag1 = 0
for digit in arr:
    if digit > flag1:
        flag1 = digit

maximum = flag1
print(maximum)


flag2 = 0
for digit in arr:
    if digit < flag2:
        flag2 = digit

minimum = flag2
print(minimum)