def one_d_matrix(m):
    one_d_array = []

    for row in m:
        for element in row:
            one_d_array.append(element)

    return one_d_array

matrix1 = [
    [2, 3],
    [1, 5]
]

matrix2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

matrix3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

flat1 = one_d_matrix(matrix1)
flat2 = one_d_matrix(matrix2)
flat3 = one_d_matrix(matrix3)

print(*flat1)
print(*flat2)
print(*flat3)