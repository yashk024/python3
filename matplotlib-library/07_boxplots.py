import numpy as np
import matplotlib.pyplot as plt

# normal distribution with
# mean=172, standard_deviation=8,
# and 300 heights to be generated
heights = np.random.normal(172, 8, 300)

plt.boxplot(heights)

plt.show()
