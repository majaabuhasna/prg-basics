import checker

number = int(input('A number: '))
number1 = 2
number2 = 15

if checker.number_in_range(number, number1, number2):
    print(f"Number {number} in range <{number1},{number2}>: yes")
else:
    print(f"Number {number} in range <{number1},{number2}>: no")