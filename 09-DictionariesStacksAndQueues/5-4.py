winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

total = 0
for values in winter_semester.values():
    total += values

print(f'The total number of hours in the winter semester is {total}')