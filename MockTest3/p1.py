def f(word):
    result = []

    for i in range(len(word)):
        waved = word.lower()
        waved = waved[:i] + waved[i].upper() + waved[i+1:]
        result.append(waved)

    return "-".join(result)

print(f('water'))