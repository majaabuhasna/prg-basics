results = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
   return lambda pts: pts>=limit

p70 = list(filter(min_pts(70),results))
print(f'Min 70 pts: {p70}')

p40 = list(filter(min_pts(40),results))
print(f'Min 40 pts: {p40}')

p30 = list(filter(min_pts(30),results))
print(f'Min 30 pts: {p30}')