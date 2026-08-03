import numpy as np
import matplotlib.pyplot as plt

omega = 10
zeta = 0.2
F = 1
x = 0
z = 0

h = 0.01
T = 5

time = np.arange(0, T + h, h)

X = []
Z = []
print("Time\tDisplacement\tVelocity")
print("--------------------------------")

for i, t in enumerate(time):

    X.append(x)
    Z.append(z)

    k1 = h * z
    l1 = h * (omega**2 * F - 2 * zeta * omega * z - omega**2 * x)

    xp = x + k1
    zp = z + l1

    k2 = h * zp
    l2 = h * (omega**2 * F - 2 * zeta * omega * zp - omega**2 * xp)

    k = (k1 + k2) / 2
    l = (l1 + l2) / 2


    x = x + k
    z = z + l


    if i % 50 == 0:
        print(f"{t:.1f}\t{x:.4f}\t\t{z:.4f}")

plt.plot(time, X)
plt.xlabel("Time (s)")
plt.ylabel("Displacement x(t)")
plt.title("Spring-Mass-Damper Response using RK2")
plt.grid(True)
plt.show()
