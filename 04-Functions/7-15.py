def f(detector):
    i = 0
    for char in str(detector):
        if char == '+':
            i += 1
            if i >= 3:
                return True
        elif char == '-':
            i -= 1
    return False

print(f("+-+++-+---"), f("+-+-+-+-"), f("+-++-+--"), f("+-++-++-+---"), sep="\n")
