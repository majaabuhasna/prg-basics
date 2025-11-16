def f(detector):
    i = 0
    for char in str(detector):
        if char == '+':
            i += 1
            if i >= 3:
                return print(True)
        elif char == '-':
            i -= 1
    return print(False)

f("+-+++-+---")
f("+-+-+-+-")
f("+-++-+--")
f("+-++-++-+---")
