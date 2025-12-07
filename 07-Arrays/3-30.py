arr = [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]
       ]

for row in range(5):
    for column in range(5):

        arr[row][column] = (row + 1) * (column + 1)

for row in arr:
    print(*row)