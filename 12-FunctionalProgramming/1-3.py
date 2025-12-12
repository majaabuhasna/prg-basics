def ms_to_kmh(ms):
    kmh = 3.6 * int(ms)
    return kmh

ms1 = 10
ms2 = 35

kmh1 = ms_to_kmh(ms1)
kmh2 = ms_to_kmh(ms2)

print(f'{ms1} m/s = {kmh1} km/h')
print(f'{ms2} m/s = {kmh2} km/h')