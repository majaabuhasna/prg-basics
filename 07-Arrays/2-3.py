# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements

food_expenses = 0
transport_expenses = 0
utilities_expenses = 0

weekly_sums = []
total = 0

for week in monthly_expenses:
    food_expenses += week[0]
    transport_expenses += week[1]
    utilities_expenses += week[2]

    current_week_sum = 0
    for expense in week:
        current_week_sum += expense

    weekly_sums.append(current_week_sum)

    total += current_week_sum


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food_expenses)
print('Transport:',transport_expenses)
print('Utilities:',utilities_expenses)
print('Week 1:',weekly_sums[0])
print('Week 2:',weekly_sums[1])
print('Week 3:',weekly_sums[2])
print('Week 4:',weekly_sums[3])
print('---------------')
print('TOTAL:',total)