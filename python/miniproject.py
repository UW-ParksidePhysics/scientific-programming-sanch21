# Initial velocity (v0) = 2 m/s
# Initial height   (h0) = 5 m
# Gravity          (g)  = 9.81 m/s
# Height of pulley (H)  = 10 m
# Radius of pulley (R)  = 1 m
# Length of rope   (L)  = 15 m
# Masses           (m1) = 2 kg
#                  (m2) = 5 kg

from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt

m1 = 2
m2 = 5
g = -9.81
v0 = 2
a = ((m2 - m1) * g) / (m1 + m2)
t = linspace(0, 10)


def height(time):
    h = v0 * time + 0.5 * a * time ** 2
    return h


heights = height(t)
print(heights)

plt.plot(t, heights)
plt.show()
