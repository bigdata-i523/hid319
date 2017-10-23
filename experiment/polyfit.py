import matplotlib.pyplot as plt
import numpy as np

n = 100
x = np.random.randn(n)
y = x * np.random.randn(n)
print x
color1 = ['blue', 'red', 'green', 'black', 'yellow', 'orange', 'pink', 'grey', 'violet', 'indigo']
figure, ax = plt.subplots()
for i in range(1,10):
    fit = np.polyfit(x, y, deg=i)
    ax.plot(x, fit[0] * x + fit[1], color=color1[i])
    ax.scatter(x, y)

plt.show()
