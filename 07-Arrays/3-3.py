arr = [8,2,5,1,9]

arr2 = []

for digit in arr:
    digit_squared = digit * digit
    arr2.append(digit_squared)

print(arr2)

arr3 = [digit * digit for digit in arr]
print(arr3)