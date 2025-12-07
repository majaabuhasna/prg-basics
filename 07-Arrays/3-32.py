arr = [
    [3,2,5,6,2],
    [1,2,9,0,0],
    [5,3,7,2,1]
]

print(f'Before: {arr}')

arr[0], arr[2] = arr[2], arr[0]

print(f'After: {arr}')