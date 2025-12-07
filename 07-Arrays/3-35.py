def transpose_matrix(m):
    rows = len(m)
    columns = len(m[0])

    transposed = []

    for i in range(columns):
        new_row = []
        for row in m:
            new_row.append(row[i])
        transposed.append(new_row)

    return transposed

first_matrix = [[1,2,3],[4,5,6],[7,8,9]]
second_matrix = [[1,2,3,4,5],[6,7,8,9,0]]
third_matrix = [[5,6,7,8]]

print('First matrix:')
for row in first_matrix:
    print(*row)

print()

print('First matrix transposed:')
for row in transpose_matrix(first_matrix):
    print(*row)

print()

print('Second matrix:')
for row in second_matrix:
    print(*row)

print()

print('Second matrix transposed:')
for row in transpose_matrix(second_matrix):
    print(*row)

print()

print('Third matrix:')
for row in third_matrix:
    print(*row)

print()

print('Third matrix transposed:')
for row in transpose_matrix(third_matrix):
    print(*row)