def identity_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(0)

        matrix.append(row)

    for i in range(n):
        matrix[i][i] = 1

    return matrix

my_matrix = identity_matrix(8)

for row in my_matrix:
    print(*row)