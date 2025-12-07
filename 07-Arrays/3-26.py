import matplotlib.pyplot as plt
import math

x = []
y = []

for n in range(0,361):
    x.append(n)

    rads = math.radians(n)

    result = math.sin(rads)

    y.append(result)

plt.plot(x, y)
plt.show()