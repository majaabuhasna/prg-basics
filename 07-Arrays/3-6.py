arr = [15, 8, 31, 47, 2, 19]

sum = 0
i = 0
while i < len(arr):
    sum += arr[i]
    i += 1

arithmetic = sum / len(arr)

print(f'{arithmetic:.2f}')