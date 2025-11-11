x = int(input('x = '))
y = int(input('y = '))

if x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")

elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")

elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")

elif x > 0 and y < 0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")

else:
    print(f"Point P({x},{y}) is located in the position (0,0) of the coordinate system")