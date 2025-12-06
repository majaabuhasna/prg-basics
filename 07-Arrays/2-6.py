x = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

i = 0

for row in x:
    row[i] = 1
    i += 1

    for digit in row:
        print(digit,end=" ")
    print()