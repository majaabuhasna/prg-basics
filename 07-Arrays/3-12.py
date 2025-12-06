arr = [2,3,2,5,8,1,9,8]
unique = []

for i in range(0,10):
    if arr.count(i) == 1:
        unique.append(i)
    else:
        continue

print(unique)