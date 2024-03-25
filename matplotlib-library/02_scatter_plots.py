import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

# plt.scatter(x_data, y_data)
# plt.scatter(x_data, y_data, c="#000")
# plt.scatter(x_data, y_data, c="red")
plt.scatter(x_data, y_data, marker="*", s=100, alpha=0.50)

plt.show()
