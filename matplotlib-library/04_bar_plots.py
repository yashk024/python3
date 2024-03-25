import matplotlib.pyplot as plt

x = ["C++", "C#", "Python", "Java", "Go"]
y = [20, 50, 140, 1, 45]  # votes

# plt.bar(x, y)
plt.bar(x, y, color="g", align="edge", width=0.5, edgecolor="red", lw=2)

plt.show()
