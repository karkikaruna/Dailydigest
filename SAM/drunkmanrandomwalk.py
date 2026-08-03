import random
import math
import matplotlib.pyplot as plt


steps = int(input("Enter the number of steps: "))


x, y = 0, 0


x_points = [x]
y_points = [y]

for i in range(steps):
    direction = random.choice(['up', 'down', 'left', 'right'])

    if direction == 'up':
        y += 1
    elif direction == 'down':
        y -= 1
    elif direction == 'left':
        x -= 1
    else:
        x += 1

    x_points.append(x)
    y_points.append(y)

distance = math.sqrt(x**2 + y**2)

print("\nFinal Position: ({}, {})".format(x, y))
print("Distance from Origin = {:.3f}".format(distance))

plt.figure(figsize=(7,7))
plt.plot(x_points, y_points, marker='o', markersize=3, linewidth=1)

plt.scatter(0, 0, color='green', s=80, label='Start')
plt.scatter(x, y, color='red', s=80, label='End')

plt.title("Drunk Man Random Walk")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.axis('equal')
plt.legend()

plt.show()