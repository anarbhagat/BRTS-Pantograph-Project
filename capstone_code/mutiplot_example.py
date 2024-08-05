import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
x = np.linspace(-2, 2, 10)
y1 = np.sin(x)
y2 = np.cos(x)
plt.subplot(211)
plt.plot(y1)
plt.subplot(212)
plt.plot(y2)
plt.show()