import numpy as np
import matplotlib.pyplot as plt


file_path = "/home/jeongil/collision/making_file/2dof_2D_graph_data.txt"

x_values = []
y_values = []
z_values = []

with open(file_path, "r") as file:
    for line in file:
        data = line.strip().split(",")
        x = float(data[0])
        y = float(data[1])
        z = float(data[2])
        x_values.append(x)
        y_values.append(y)
        z_values.append(z)

x_unique = np.sort(np.unique(x_values))
y_unique = np.sort(np.unique(y_values))
z_array = np.zeros((len(y_unique), len(x_unique)))

for x, y, z in zip(x_values, y_values, z_values):
    x_index = np.where(x_unique == x)[0][0]
    y_index = np.where(y_unique == y)[0][0]
    z_array[y_index, x_index] = z

plt.imshow(z_array, cmap='Pastel1', origin='upper', extent=[x_unique[0], x_unique[-1], y_unique[0], y_unique[-1]])

plt.xlabel("joint 1 angle(q1, degrees)")
plt.ylabel("joint 2 angle(q2, degrees)")

plt.title("C-space")
plt.show()