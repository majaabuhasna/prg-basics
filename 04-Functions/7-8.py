def f(amount_to_pay):
    amount_to_pay = int(amount_to_pay)
    coins = 0

    while amount_to_pay >= 5:
        coins = amount_to_pay // 5
        rest = amount_to_pay % 5
        amount_to_pay = rest

    while amount_to_pay >= 2:
        coins = coins + (amount_to_pay // 2)
        rest = amount_to_pay % 2
        amount_to_pay = rest

    while amount_to_pay >= 1:
        coins = coins + (amount_to_pay // 1)
        rest = amount_to_pay % 1
        amount_to_pay = rest

    while amount_to_pay == 0:
        break
        
    return coins

print(f(23))
print(f(8))
print(f(2))
print(f(0))