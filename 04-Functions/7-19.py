def f(number):
    number = str(number)
    sum = 0
    for digit in number:
        if number.count(digit) > 1:
            sum += int(digit)
    return sum

print(f(1027), f(230335), f(513553007), sep="\n")