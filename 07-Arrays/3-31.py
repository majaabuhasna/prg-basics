arr = [[-38, 19], [5,40],[-7,11],[29,16]]

largest = float('-inf')
smallest = float('inf')

for row in arr:
    for digit in row:
        if digit > largest:
            largest = digit
            row_number_largest = arr.index(row) + 1
            column_number_largest = row.index(largest) + 1

        if digit < smallest:
            smallest = digit
            row_number_smallest = arr.index(row) + 1
            column_number_smallest = row.index(smallest) + 1

print(f'Largest number ({largest}) is in row {row_number_largest} and column {column_number_largest}')
print(f'Smallest number ({smallest}) is in row {row_number_smallest} and column {column_number_smallest}')

