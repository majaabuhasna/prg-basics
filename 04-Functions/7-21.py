def f(number1,number2,number3):
    max_number = max(number1,number2,number3)
    min_number = min(number1,number2,number3)

    difference = max_number - min_number
    return difference

print(f(7,4,9), f(2,12,8), sep="\n")