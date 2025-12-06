arr = [15, 8, 31, 47, 2, 19]

sum = 0
for digit in arr:
    sum += digit

arithmetic = sum / len(arr)

print(f'{arithmetic:.2f}')