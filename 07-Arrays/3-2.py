arr = [15, 8, 31, 47, 2, 19]
arr_reversed = []

i = 0
j = -1
while i < len(arr):
    x = arr[j]
    i += 1
    j -= 1

    arr_reversed.append(x)

print(arr_reversed)

arr_reversed2 = arr[::-1]
print(arr_reversed2)

arr_reversed3 = list(reversed(arr))
print(arr_reversed3)