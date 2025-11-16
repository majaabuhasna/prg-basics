def f(number, even):
    sum = 0
    number = str(number)
    if even == True:
        for digit in number:
            digit = int(digit)
            if digit % 2 == 0:
                sum += digit
        return sum
    if even == False:
        for digit in number:
            digit = int(digit)
            if digit % 2 != 0:
                sum += digit
        return sum

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))