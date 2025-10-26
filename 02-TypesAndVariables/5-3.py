###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

cuboid_volume = a*b*c
cuboid_surface_area = 2*(a*b + b*c + c*a)

print(f'The volume of a cuboid with sides {a}, {b} and {c} is {cuboid_volume}')
print(f'The surface area of a cuboid with sides {a}, {b} and {c} is {cuboid_surface_area}')