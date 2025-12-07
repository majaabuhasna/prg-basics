arr = [
    [3,2,5,6,2],
    [1,2,9,0,0],
    [5,3,7,2,1]
]

print(f'Before: {arr}')

for row in arr:
    row[0], row[4] = row[4], row[0]

print(f'After: {arr}')