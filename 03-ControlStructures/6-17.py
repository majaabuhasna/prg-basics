hour_24 = input("Enter time (24-hour format): ")

h24 = int(hour_24[0:2])
m24 = int(hour_24[3:5])

h12 = 0
m12 = m24
index = ''

if h24 > 0 and h24 < 12:
    h12 = h24
    index = 'am'

elif h24 == 12:
    h12 = 12
    index = 'pm'

elif h24 >= 12 and h24 < 24:
    if h24 == 13:
        h12 = 1
    if h24 == 14:
        h12 = 2
    if h24 == 15:
        h12 = 3
    if h24 == 16:
        h12 = 4
    if h24 == 17:
        h12 = 5
    if h24 == 18:
        h12 = 6
    if h24 == 19:
        h12 = 7
    if h24 == 20:
        h12 = 8
    if h24 == 21:
        h12 = 9
    if h24 == 22:
        h12 = 10
    if h24 == 23:
        h12 = 11
    index = 'pm'

elif h24 == 24:
    h12 = 12
    index = 'am'

print(f"Time in 12-hour format: {h12:02d}:{m12:02d}{index}")