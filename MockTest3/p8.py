def f(fnc,prods):
    text = []
    for product in prods:
        text.append(fnc(product))

    return ','.join(text)

prods1 = ["water","cheese","tomato"]
fnc1 = lambda x: "id:"+x[:2]
fnc2 = lambda x: (x[0]+x[-1]).upper()

print(f(fnc1,prods1))
print(f(fnc2,prods1))