arr = [7,9,2,4,5,6]

even = []
odd = []

for digit in arr:
    if digit % 2 == 0:
        even.append(digit)
    else:
        odd.append(digit)

new_arr = even + odd

print(f'arr = {arr}')
print(f'arr = {new_arr}')