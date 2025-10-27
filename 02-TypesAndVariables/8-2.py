###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

radius = float(input('Enter circle radius: '))

pi = 3.14
circle_area = radius**2 * pi
circle_circumference = 2 * radius * pi

print(f'Circle area:{circle_area: .2f}')
print(f'Circle circumference:{circle_circumference: .2f}')