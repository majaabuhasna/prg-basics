categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

maximum_expense = max(expenses)

index = expenses.index(maximum_expense)

print('The most expensive category is:', categories[index])