avg_speed = lambda distance,hours,minutes: distance/((minutes/60)+hours)

d1 = int(input('Enter distance: '))
h1 = int(input('Enter number of travel hours: '))
m1 = int(input('Enter number of travel minutes: '))

avg1 = avg_speed(d1,h1,m1)

print(f'Average speed: {avg1:.1f} km/h')
