import numpy as np
import matplotlib.pyplot as plt

# normal distribution with
# mean=20, standard_deviation=1.5
# 1000 different values to be generated
ages = np.random.normal(20, 1.5, 1000)
# print(ages)

# plt.hist(ages)
plt.hist(ages, bins=20)
# plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()])
# plt.hist(ages, bins=20, cumulative=True)
plt.show()
