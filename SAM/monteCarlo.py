import random
import math
import matplotlib.pyplot as plt

N = int(input("Enter the number of random points: "))

inside_circle = 0

x_inside = []
y_inside = []
x_outside = []
y_outside = []

# Monte Carlo Simulation
for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

pi_estimate = 4 * inside_circle / N

error = abs(math.pi - pi_estimate) / math.pi * 100

print("\nEstimated Value of Pi =", pi_estimate)
print("Actual Value of Pi    ={:.5f}" .format(math.pi))
print("Percentage Error      = {:.5f}%".format(error))

# Plot
plt.figure(figsize=(6,6))
plt.scatter(x_inside, y_inside, s=2, color='green', label='Inside Circle')
plt.scatter(x_outside, y_outside, s=2, color='blue', label='Outside Circle')

circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
plt.gca().add_artist(circle)

plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.gca().set_aspect('equal')

plt.title("Monte Carlo Simulation for Estimation of Pi")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.show()