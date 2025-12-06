x = [34,7,19,4,21,8]

sum = 0
for digit in x:
    if digit % 2 == 0:
        sum += digit

print(sum)